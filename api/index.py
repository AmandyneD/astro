from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Birth(BaseModel):
    date: str  # "YYYY-MM-DD"

def zodiac_sign(month: int, day: int) -> str:
    # Dates "classiques" astrologie occidentale
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Bélier"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taureau"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gémeaux"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Lion"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Vierge"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Balance"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpion"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittaire"
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorne"
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Verseau"
    return "Poissons"  # (month == 2 and day >= 19) or (month == 3 and day <= 20)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/zodiac")
def zodiac(payload: Birth):
    try:
        dt = datetime.strptime(payload.date, "%Y-%m-%d")
    except Exception:
        return {"error": "Format invalide. Utilise YYYY-MM-DD (ex: 1994-07-12)"}

    sign = zodiac_sign(dt.month, dt.day)
    return {"sign": sign}
