import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

def zodiac_sign(month: int, day: int) -> str:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Bélier"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taureau"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gémeaux"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Lion"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Vierge"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Balance"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpion"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittaire"
    if (month == 12 and day >= 22) or (month == 1 and day <= 19): return "Capricorne"
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Verseau"
    return "Poissons"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"

        try:
            payload = json.loads(raw)
            date_str = payload.get("date", "")
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            sign = zodiac_sign(dt.month, dt.day)
            resp = {"sign": sign}
            code = 200
        except Exception:
            resp = {"error": "Date invalide. Format attendu: YYYY-MM-DD (ex: 1991-08-13)"}
            code = 400

        body = json.dumps(resp).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)
