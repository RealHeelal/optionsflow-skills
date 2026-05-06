---
name: pop-validator
description: Validates that Probability of Profit meets the 55% minimum before any trade recommendation.
---

## Purpose
Check POP = 1 - Delta. Reject trades below 55% minimum.

## Logic
```python
def validate(delta: float) -> dict:
    pop = round((1 - delta) * 100, 1)
    if pop < 55:
        better = round(1 - 0.55, 2)
        return {
            "status": "REJECTED",
            "message": f"⛔ POP {pop}% < 55% الحد الأدنى\nجرب Delta ≤ {better} للحصول على POP ≥ 55%"
        }
    return {
        "status": "PASS",
        "message": f"✅ POP: {pop}% — فوق الحد الأدنى"
    }
```

## Output Format
- REJECTED: show message, suggest better strike
- PASS: show "✅ POP: [X]%"
