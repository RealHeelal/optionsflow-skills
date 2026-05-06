---
name: bankroll-gate
description: Validates trade cost against bankroll limits before any recommendation. Calculates Ask x 100 and blocks trades that exceed dollar limits.
---

## Purpose
Calculate the real cost of an options contract and enforce bankroll limits.

## Rules
- Scalp 0DTE: MAX $25 (Ask × 100 ≤ 0.25)
- Swing 5+DTE: MAX $50 (Ask × 100 ≤ 0.50)
- Full Stack: MAX $100 (Ask × 100 ≤ 1.00)
- Always multiply Ask × 100 — never use % of $500

## Logic
```python
def check(ask_price: float, trade_type: str) -> dict:
    cost = round(ask_price * 100, 2)
    limits = {"scalp": 25, "swing": 50, "stack": 100}
    limit = limits.get(trade_type, 25)
    if cost > limit:
        return {
            "status": "BLOCKED",
            "message": f"⛔ SCALP BLOCKED\nAsk ${ask_price} × 100 = ${cost}\nLimit = ${limit}\n${cost} > ${limit} — لا يمكن الدخول\n\nالحلول:\n1. انتظر Premium ≤ ${limit/100}\n2. استخدم slot أعلى\n3. ابحث عن سهم بديل"
        }
    return {
        "status": "PASS",
        "message": f"✅ Bankroll Cost: ${cost} out of ${limit} — FITS"
    }
```

## Output Format
- BLOCKED: show full block message and STOP
- PASS: show "✅ Bankroll Cost: $[Y] out of $[limit]" and continue
