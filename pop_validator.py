# pop_validator.py
def validate_pop(delta):
    pop = round((1 - delta) * 100, 1)
    minimum = 55
    if pop < minimum:
        better_delta = round(1 - (minimum/100), 2)
        return {
            "status": "REJECTED",
            "pop": pop,
            "message": f"⛔ POP {pop}% < 55% الحد الأدنى\n"
                      f"جرب Delta ≤ {better_delta} للحصول على POP ≥ 55%"
        }
    return {
        "status": "PASS",
        "pop": pop,
        "message": f"✅ POP: {pop}% — فوق الحد الأدنى"
    }
