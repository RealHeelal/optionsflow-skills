# top_pick_enforcer.py
def validate_top_pick(tickers_with_scores):
    # tickers_with_scores = [{"ticker":"NVDA","score":9}, ...]
    eligible = [t for t in tickers_with_scores if t["score"] >= 7]
    
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
