# Review a customer quote

## What this process does

Prepare a draft quote from a customer's request, obtain a person's decision, and record the outcome. Use this process when a request is ready for pricing. This is a workshop authoring example, not a deployed integration; configure assignments, skills, tools, and access before use.

## Steps

### Step 1 -- Prepare the draft

**Input:** `request_details`, `price_list`

**Processing:** Check that the request includes the work, location, and requested date. If information is missing, stop and ask the requester to supply it. Prepare the scope and price from the supplied price list. Do not send a quote to the customer.

**Output (process state):**
```json
{
  "draft_quote": {"scope": "Proposed work", "price": 0, "currency": "CAD"}
}
```

### Step 2 -- Review the draft

**Input:** `draft_quote`

**Processing:** A person with the business's approval authority reviews the scope and price. Record whether the quote is approved and explain the decision. If it needs changes, reject it and record the changes needed; do not silently replace the draft or send it to the customer.

**Output (process state):**
```json
{
  "approval_decision": {"approved": false, "reason": "Reason for the decision"}
}
```

### Step 3 -- Record the outcome

**Input:** `draft_quote`, `approval_decision`

**Required Resources:** `quote records workspace`

**Processing:** Save the exact draft and decision in the quote records workspace. Mark rejected drafts as requiring changes. Record the path only after the save succeeds; if the save fails, report the failure without claiming completion. Sending a quote to the customer is outside this process.

**Output (process state):**
```json
{
  "quote_record_path": "Path of the saved quote and decision"
}
```

## Variables

| Variable | Type | Description |
| --- | --- | --- |
| `request_details` | object | Customer's requested work, location, and date, supplied at the start |
| `price_list` | object | Current prices and pricing rules, supplied at the start |
| `draft_quote` | object | Proposed scope and price, produced by Step 1 |
| `approval_decision` | object | Approval or rejection and its reason, produced by Step 2 |
| `quote_record_path` | string (path) | Path of the saved draft and decision, produced by Step 3 |
