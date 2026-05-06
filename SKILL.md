---
name: top-pick-enforcer
description: Ensures only ONE ticker is labeled TOP PICK per report, and only if Score >= 7.
---

## Purpose
Enforce single TOP PICK rule at end of every morning report.

## Logic
```python
def enforce(tickers: list) -> dict:
    # tickers = [{"ticker": "NVDA", "score": 9}, ...]
    eligible = [t for t in tickers if t["score"] >= 7]
    if not eligible:
        return {
            "status": "NO_PICK",
            "message": "⛔ لا يوجد TOP PICK اليوم — كل الأسهم Score أقل من 7"
        }
    best = max(eligible, key=lambda x: x["score"])
    return {
        "status": "ONE_PICK",
        "ticker": best["ticker"],
        "score": best["score"],
        "message": f"🏆 TOP PICK: {best['ticker']} — Score {best['score']}/10"
    }
```

## Output Format
- ONE_PICK: show only the single highest score ticker
- NO_PICK: show the Arabic rejection message
