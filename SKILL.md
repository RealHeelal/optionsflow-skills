---
name: morning-validator
description: Validates morning report completeness. Checks that RISK LEVEL is line 1 and all required sections exist.
---

## Purpose
Verify morning report follows mandatory template before sending.

## Required Sections
1. RISK LEVEL (must be LINE 1)
2. POLITICAL MONITOR
3. EARNINGS THIS WEEK
4. BLACKOUT
5. SPY + QQQ
6. TOP PICK or NO PICK message

## Logic
```python
def validate(report: str) -> dict:
    errors = []
    lines = report.strip().split('\n')
    if "RISK LEVEL" not in lines:
        errors.append("❌ RISK LEVEL not on line 1")
    for section in ["POLITICAL MONITOR", "EARNINGS THIS WEEK", "BLACKOUT", "SPY", "TOP PICK"]:
        if section not in report:
            errors.append(f"❌ MISSING: {section}")
    if errors:
        return {"status": "INVALID", "errors": errors}
    return {"status": "VALID", "message": "✅ Report complete — جاهز للإرسال"}
```

## Output Format
- INVALID: list all missing sections
- VALID: confirm report is complete
