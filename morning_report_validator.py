# morning_report_validator.py
def validate_report(report_text):
    errors = []
    
    # Check LINE 1
    first_line = report_text.strip().split('\n')[0]
    if "RISK LEVEL" not in first_line:
        errors.append("❌ VIOLATION: RISK LEVEL not on line 1")
    
    # Check required sections
    required = [
        "POLITICAL MONITOR",
        "EARNINGS THIS WEEK",
        "BLACKOUT",
        "SPY",
        "TOP PICK"
    ]
    for field in required:
        if field not in report_text:
            errors.append(f"❌ MISSING: {field}")
    
    if errors:
        return {"status": "INVALID", "errors": errors}
    return {"status": "VALID", "message": "✅ Report complete"}
