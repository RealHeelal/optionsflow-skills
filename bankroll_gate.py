# bankroll_gate.py
def check_scalp(ask_price):
    cost = round(ask_price * 100, 2)
    limit = 25
    if cost > limit:
        return {
            "status": "BLOCKED",
            "message": f"⛔ SCALP BLOCKED\n"
                      f"Ask ${ask_price} × 100 = ${cost}\n"
                      f"Limit = $25\n"
                      f"${cost} > $25 — لا يمكن الدخول\n\n"
                      f"الحلول:\n"
                      f"1. انتظر Premium ≤ $0.25\n"
                      f"2. استخدم Swing slot ($50 max)\n"
                      f"3. ابحث عن سهم بديل"
        }
    return {
        "status": "PASS",
        "message": f"✅ Bankroll Cost: ${cost} out of $25 — FITS"
    }

def check_swing(ask_price):
    cost = round(ask_price * 100, 2)
    limit = 50
    if cost > limit:
        return {"status": "BLOCKED",
                "message": f"⛔ SWING BLOCKED: ${ask_price}×100=${cost} > $50"}
    return {"status": "PASS",
            "message": f"✅ Swing Cost: ${cost} out of $50 — FITS"}

def check_fullstack(ask_price):
    cost = round(ask_price * 100, 2)
    limit = 100
    if cost > limit:
        return {"status": "BLOCKED",
                "message": f"⛔ FULL STACK BLOCKED: ${ask_price}×100=${cost} > $100"}
    return {"status": "PASS",
            "message": f"✅ Full Stack Cost: ${cost} out of $100 — FITS"}
