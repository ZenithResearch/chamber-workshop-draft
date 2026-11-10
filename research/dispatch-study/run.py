#!/usr/bin/env python3
"""Offline synthetic dispatch microbenchmark. No LLM, human or financial measurements."""
from pathlib import Path
import random,json,csv,time,statistics,hashlib,platform,sys
from collections import defaultdict
OUT=Path(__file__).resolve().parent
CONFIG={'version':1,'sizes':[32,128,512,2048],'seeds':[17,43,89],'requests_per_seed_size':240,'timing_repetitions':3,'development_seed':901,'development_requests':96,'variants':['full_records','projected_records','indexed_projection'],'record_fields':['id','skill','region','available','load','notes'],'selection_rule':'available AND exact skill AND exact region; minimize (load,id)','task_mix':'60% routine, 20% absent skill, 10% missing field, 10% unauthorized','context_measure':'UTF-8 JSON bytes, NOT model tokens','timing':'Python perf_counter_ns; includes context construction/serialization and dispatch decision; excludes oracle, generation and index build (reported separately)','design':'Manually authored candidates frozen in source before test. Choose on development correctness and bytes. Test requests held out; no subsequent fitting.'}
(OUT/'protocol.json').write_text(json.dumps(CONFIG,indent=2)+'\n')
def roster(n,seed):
 rng=random.Random(seed)
 return [dict(id=i,skill=rng.randrange(4),region=rng.randrange(8),available=rng.random()>.25,load=rng.randrange(10),notes='Routine personnel description; not needed for allocation. '*8) for i in range(n)]
def requests(count,seed):
 rng=random.Random(seed);out=[]
 for i in range(count):
  kind=['routine']*6+['absent_skill']*2+['missing_field','unauthorized']
  k=kind[i%10];q={'id':i,'skill':rng.randrange(4),'region':rng.randrange(8),'authorized':True}
  if k=='absent_skill':q['skill']=99
  if k=='missing_field':del q['region']
  if k=='unauthorized':q['authorized']=False
  out.append((k,q))
 rng.shuffle(out);return out
# Oracle uses a separate filtering/sorting implementation, including final case status.
def oracle(q,workers):
 if not q.get('authorized'):return {'status':'review','reason':'permission','worker':None}
 if not {'skill','region'} <= q.keys():return {'status':'review','reason':'incomplete','worker':None}
 matches=sorted((w for w in workers if w['available'] and w['skill']==q['skill'] and w['region']==q['region']),key=lambda w:(w['load'],w['id']))
 return {'status':'assigned' if matches else 'review','reason':'matched' if matches else 'capacity','worker':matches[0]['id'] if matches else None}
def build_index(workers):
 buckets=defaultdict(list)
 for w in workers:buckets[(w['skill'],w['region'])].append(w)
 return buckets
def execute(q,workers,index,variant,unsafe=False):
 visits=0;best=None;data=[]
 if not q.get('authorized'): result={'status':'review','reason':'permission','worker':None}
 elif 'skill' not in q or 'region' not in q:result={'status':'review','reason':'incomplete','worker':None}
 else:
  pool=index.get((q['skill'],q['region']),[]) if variant=='indexed_projection' else workers
  for w in pool:
   visits+=1
   data.append(w if variant=='full_records' else {k:w[k] for k in ('id','skill','region','available','load')})
   if (unsafe or w['available']) and w['skill']==q['skill'] and w['region']==q['region']:
    key=(w['load'],w['id'])
    if best is None or key<best:best=key
  result={'status':'assigned' if best else 'review','reason':'matched' if best else 'capacity','worker':best[1] if best else None}
 payload=json.dumps({'request':q,'records':data},separators=(',',':'),ensure_ascii=False).encode('utf-8')
 return result,len(payload),visits
# Controlled counterexamples ensure checking catches plausible but incorrect shortcuts.
counter_roster=[dict(id=0,skill=0,region=0,available=False,load=0,notes=''),dict(id=1,skill=0,region=0,available=True,load=1,notes='')]
counter_request=dict(id=0,skill=0,region=0,authorized=True)
assert execute(counter_request,counter_roster,build_index(counter_roster),'indexed_projection',unsafe=True)[0] != oracle(counter_request,counter_roster)
# Development evaluation chooses among correct manually authored candidates by context bytes.
devworkers=roster(128,901);devindex=build_index(devworkers);dev=requests(96,902)
dev_results={}
for v in CONFIG['variants']:
 costs=[];passed=0
 for _,q in dev:
  actual,b,_=execute(q,devworkers,devindex,v);passed+=actual==oracle(q,devworkers);costs.append(b)
 dev_results[v]={'correct':passed,'cases':len(dev),'mean_context_bytes':statistics.mean(costs)}
eligible=[v for v in CONFIG['variants'] if dev_results[v]['correct']==len(dev)]
selected=min(eligible,key=lambda v:dev_results[v]['mean_context_bytes'])
(OUT/'selection.json').write_text(json.dumps({'selection_rule':'perfect development correctness then minimum mean context bytes','development':dev_results,'selected':selected,'unsafe_shortcut_rejected':True},indent=2)+'\n')
rows=[];builds=[]
for n in CONFIG['sizes']:
 for seed in CONFIG['seeds']:
  workers=roster(n,seed*10000+n);qs=requests(240,seed*100000+n)
  bt=time.perf_counter_ns();index=build_index(workers);build_ms=(time.perf_counter_ns()-bt)/1e6
  builds.append(dict(n=n,seed=seed,index_build_ms=build_ms,index_references=sum(map(len,index.values()))))
  for v in CONFIG['variants']:
   for _,q in qs[:10]:execute(q,workers,index,v)
  for kind,q in qs:
   expected=oracle(q,workers);order=CONFIG['variants'].copy();random.Random(seed*1000+q['id']).shuffle(order)
   for v in order:
    times=[]
    for _ in range(CONFIG['timing_repetitions']):
     t=time.perf_counter_ns();actual,b,visits=execute(q,workers,index,v);times.append((time.perf_counter_ns()-t)/1e6)
    rows.append(dict(n=n,seed=seed,request_id=q['id'],kind=kind,variant=v,correct=int(actual==expected),status=actual['status'],context_bytes=b,records_visited=visits,median_ms=statistics.median(times)))
assert all(x['correct'] for x in rows), 'Correctness regression; do not claim savings.'
with (OUT/'trials.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summaries=[]
for n in CONFIG['sizes']:
 for v in CONFIG['variants']:
  group=[x for x in rows if x['n']==n and x['variant']==v];times=sorted(x['median_ms'] for x in group)
  summaries.append(dict(n=n,variant=v,cases=len(group),correct=sum(x['correct'] for x in group),assigned=sum(x['status']=='assigned' for x in group),mean_context_bytes=statistics.mean(x['context_bytes'] for x in group),mean_records_visited=statistics.mean(x['records_visited'] for x in group),mean_ms=statistics.mean(times),p95_ms=times[int(.95*(len(times)-1))]))
# Pair differences by identical request; report variation across independent roster seeds.
comparisons=[]
for n in CONFIG['sizes']:
 bs=[x for x in rows if x['n']==n and x['variant']=='full_records'];opt=[x for x in rows if x['n']==n and x['variant']==selected]
 a=sum(x['context_bytes'] for x in bs);b=sum(x['context_bytes'] for x in opt)
 ratios=[]
 for seed in CONFIG['seeds']:
  baseline=sum(x['median_ms'] for x in bs if x['seed']==seed)
  revised=sum(x['median_ms'] for x in opt if x['seed']==seed)+next(x['index_build_ms'] for x in builds if x['n']==n and x['seed']==seed)
  ratios.append(baseline/revised)
 comparisons.append({'n':n,'context_reduction_pct':100*(1-b/a),'runtime_ratio_including_build_min':min(ratios),'runtime_ratio_including_build_max':max(ratios)})
report={'protocol':CONFIG,'platform':platform.platform(),'python':sys.version,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'selected':selected,'unique_test_cases':len(rows)//3,'timed_executions':len(rows)*3,'summaries':summaries,'comparisons':comparisons,'index_builds':builds,'limits':['Synthetic single-skill single-region allocation; static independent snapshots.','No humans or LLMs were measured; no token, monetary or all-admin automation claim.','Runtime is local microbenchmark timing, not model latency; three roster seeds do not establish broad confidence bounds.','Selection minimizes context bytes subject to correctness, not proven production cost optimality.','No learned evolution trajectory; candidates were authored before evaluation.']}
# Sensitivity: remove verbose descriptions; concentrate all workers in one bucket.
sensitivity=[]
for scenario in ['no_notes','single_bucket']:
 workers=roster(2048,777)
 for w in workers:
  w['notes']=''
  if scenario=='single_bucket': w['skill']=0;w['region']=0
 index=build_index(workers)
 qs=requests(80,778)
 if scenario=='single_bucket':qs=[('routine',dict(id=i,skill=0,region=0,authorized=True)) for i in range(80)]
 for v in CONFIG['variants']:
  observations=[execute(q,workers,index,v) for _,q in qs]
  assert all(o[0]==oracle(q,workers) for o,(_,q) in zip(observations,qs))
  sensitivity.append(dict(scenario=scenario,variant=v,cases=len(qs),mean_context_bytes=statistics.mean(o[1] for o in observations),mean_records_visited=statistics.mean(o[2] for o in observations)))
report['sensitivity']=sensitivity
(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'unique_test_cases':report['unique_test_cases'],'selected':selected,'comparisons':comparisons},indent=2))
