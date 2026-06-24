import requests
import time

# -----------------------------
#   تنظیمات ربات
# -----------------------------
TOKEN = "توکن_واقعی_تو_اینجا"
CHAT_ID = "6763316231"   # چت آیدی شما

# -----------------------------
#   تابع ارسال پیام
# -----------------------------
def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

# پیام شروع
send("🚀 ربات NDS با موفقیت استارت شد!")

# -----------------------------
#   تابع تشخیص NDS
# -----------------------------
def detect_nds(candles):
    if len(candles) < 4:
        return False

    A = candles[-4]
    B = candles[-3]
    C = candles[-2]
    D = candles[-1]

    hh = B["high"] > A["high"] and C["high"] < B["high"]
    ll = B["low"] < A["low"] and C["low"] > B["low"]

    leg1 = abs(B["high"] - A["high"])
    leg2 = abs(C["high"] - B["high"])
    leg3 = abs(D["high"] - C["high"])

    three_legs = leg1 > 0 and leg2 > 0 and leg3 > 0

    fib = abs(C["close"] - B["close"]) / max(abs(B["close"]), 1)
    fib_ok = fib >= 0.86

    return (hh or ll) and three_legs and fib_ok

# -----------------------------
#   حلقه اصلی ربات
# -----------------------------
while True:
    candles = [
        {"high": 100, "low": 90, "close": 95},
        {"high": 110, "low": 100, "close": 105},
        {"high": 108, "low": 98, "close": 100},
        {"high": 112, "low": 102, "close": 110},
    ]

    if detect_nds(candles):
        send("🔥 سیگنال NDS شناسایی شد!")

    time.sleep(5)
