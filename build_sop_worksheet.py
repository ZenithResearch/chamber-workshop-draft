#!/usr/bin/env python3
"""Build the two-page Hub SOP worksheet and DevGraph work map.

uv run --with reportlab==5.1.0 python build_sop_worksheet.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/sop-worksheet.pdf"
NAVY, INK, GRAY, LINE = map(HexColor, ("#000080", "#202020", "#555555", "#999999"))
W, H = landscape(letter)
HUB = "https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/base/ops/processes/index.md"
DEVGRAPH = "https://github.com/ZenithResearch/devgraph/blob/6789e9e754c00339db34801a9c4615fa9276a740/ontology/workflows.md"


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=(W, H), invariant=1)
    c.setTitle("SOP Worksheet | Workshop")
    c.setAuthor("Zenith")
    c.setSubject("Hub process planning with a DevGraph Issue, Task, dependency and review exercise.")

    def text(x, y, value, size=11, font="Times-Roman", color=INK):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, H-y, value)

    def para(x, y, value, width, size=11, leading=13):
        for line in simpleSplit(value, "Times-Roman", size, width):
            text(x, y, line, size)
            y += leading

    def line(x1, y1, x2, y2):
        c.setStrokeColor(LINE)
        c.setLineWidth(0.65)
        c.line(x1, H-y1, x2, H-y2)

    def field(name, label, x, y, w, h, multiline=True, maxlen=160, border=True):
        c.acroForm.textfield(
            name=name, tooltip=label, x=x, y=H-y-h, width=w, height=h,
            fontName="Helvetica", fontSize=10, textColor=INK, fillColor=white,
            borderColor=LINE, borderWidth=0.65 if border else 0,
            forceBorder=border, borderStyle="solid", value="", maxlen=maxlen,
            fieldFlags="multiline doNotScroll" if multiline else "doNotScroll",
        )

    def header(kicker, title, subtitle):
        text(36, 29, "ZENITH", 12, "Times-Bold", NAVY)
        text(702, 29, "WORKSHOP", 9, color=GRAY)
        line(36, 40, 756, 40)
        text(36, 59, kicker, 9, color=GRAY)
        text(36, 86, title, 25, "Times-Bold", NAVY)
        text(36, 106, subtitle)

    def footer(n):
        line(36, 584, 756, 584)
        text(36, 599, "Type in the boxes and save a copy, or print and write by hand.", 9, color=GRAY)
        for x, label, url, width in [(475, "Hub schema", HUB, 56), (552, "DevGraph workflow", DEVGRAPH, 85)]:
            text(x, 599, label, 9, color=NAVY)
            c.linkURL(url, (x, 10, x+width, 23), relative=0)
        text(722, 599, f"{n} of 2", 9, color=GRAY)

    header("01  /  DEFINE AND PLAN", "Standard operating procedure",
           "Choose a recurring task. Describe the process, then plan one run of it. Keep answers brief and specific.")
    text(36, 142, "Process name", 12, "Times-Bold")
    field("process_title", "Process title: name the recurring task", 36, 151, 348, 27, False, 60)
    text(36, 202, "When is it used, and what should it produce?", 12, "Times-Bold")
    field("process_description", "What this process does: trigger and intended result", 36, 211, 348, 52, maxlen=240)
    text(36, 291, "Information used or created", 15, "Times-Bold", NAVY)
    para(36, 308, "Name every input and output. Reuse these names in the steps. Types: text, number, yes/no, list, or record.", 348, 10, 12)
    xs = [36, 144, 194, 316, 384]
    for x, label in zip(xs, ["Item name", "Type", "Meaning", "Source*"]):
        text(x+5, 345, label, 10, "Times-Bold")
    for row in range(6):
        for col, (key, limit) in enumerate([("name", 32), ("type", 14), ("description", 52), ("source", 24)]):
            field(f"variable_{row+1}_{key}", f"Information item {row+1}: {key}", xs[col]+2,
                  355+row*30, xs[col+1]-xs[col]-4, 26, maxlen=limit, border=False)
    for x in xs:
        line(x, 332, x, 533)
    for y in [332, 353, 383, 413, 443, 473, 503, 533]:
        line(36, y, 384, y)
    text(36, 551, "* At start, or the step number that creates it.", 10)
    text(36, 566, "Put systems and workspace access on page 2.", 10, color=GRAY)

    text(408, 142, "Map one run in DevGraph", 15, "Times-Bold", NAVY)
    text(408, 160, "Issue = the result to deliver. Tasks = the work that gets it done.", 10)
    text(408, 182, "Issue / What result will you deliver this time?", 11, "Times-Bold")
    field("work_issue", "DevGraph Issue: result for one run of this process", 408, 190, 348, 38, maxlen=180)
    # A containment tree: all three Tasks belong to the Issue; no ordering is implied.
    line(582, 228, 582, 239)
    line(462, 239, 702, 239)
    for task, x in enumerate([408, 528, 648], 1):
        line(x+54, 239, x+54, 249)
        text(x, 262, f"Task {task} / step {task}", 11, "Times-Bold", NAVY)
        field(f"work_task_{task}_title", f"DevGraph Task {task}: short action name", x, 271, 108, 38, maxlen=60)
        text(x, 325, "Needs task no. / none", 10)
        field(f"work_task_{task}_needs", f"Task {task}: depends on task numbers, or none", x, 333, 108, 25, False, 18)
        text(x, 375, "Done when...", 11, "Times-Bold")
        field(f"work_task_{task}_criterion", f"Task {task}: acceptance check", x, 383, 108, 48, maxlen=80)
    text(408, 449, "Use the step names from page 2. Only add real dependencies.", 10)
    text(408, 473, "Review / What evidence will show the work is complete?", 11, "Times-Bold")
    field("work_evidence", "Review evidence: result or check for each task", 408, 481, 348, 30, maxlen=140)
    text(408, 533, "Handoff / Who checks it, and who receives the result?", 11, "Times-Bold")
    field("work_handoff", "Reviewer and recipient of the result", 408, 541, 348, 30, maxlen=140)
    footer(1)
    c.showPage()

    header("02  /  WRITE THE STEPS", "How the work gets done",
           "Use one box for each step. Match input and output names to page 1. Leave unused steps blank.")
    for step, x in enumerate([36, 282, 528], 1):
        prefix = f"step_{step}_"
        text(x, 144, f"STEP {step}", 12, "Times-Bold", NAVY)
        text(x+58, 144, "Name the action", 11)
        field(prefix+"title", f"Step {step}: title", x, 153, 228, 29, False, 40)
        text(x, 202, "Person or role", 11, "Times-Bold")
        text(x+120, 202, "Skill needed", 11, "Times-Bold")
        field(prefix+"assignee", f"Step {step}: Assignee", x, 210, 108, 28, maxlen=40)
        field(prefix+"skills", f"Step {step}: Skills", x+120, 210, 108, 28, maxlen=40)
        text(x, 258, "Inputs / What must be ready?", 11, "Times-Bold")
        field(prefix+"inputs", f"Step {step}: Input variable names", x, 266, 228, 32, maxlen=80)
        text(x, 318, "What happens?", 11, "Times-Bold")
        text(x, 332, "Include checks and what to do if something fails.", 10)
        field(prefix+"processing", f"Step {step}: Processing, checks, and failure handling", x, 340, 228, 62, maxlen=210)
        text(x, 422, "Outputs / Name each result and its contents.", 11, "Times-Bold")
        field(prefix+"outputs", f"Step {step}: Output process state names and contents; or none", x, 430, 228, 32, maxlen=80)
        text(x, 482, "Required systems or workspaces", 11, "Times-Bold")
        field(prefix+"required_resources", f"Step {step}: Required Resources", x, 490, 228, 28, maxlen=75)
        text(x, 540, "Helpful resources / Optional", 11, "Times-Bold")
        field(prefix+"suggested_resources", f"Step {step}: Suggested Resources", x, 548, 228, 28, maxlen=75)
    for x in [273, 519]:
        line(x, 132, x, 576)
    footer(2)
    c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
