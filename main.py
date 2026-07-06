from market_data import get_live_price
from signal_engine import get_signal
from config import SYMBOL, UPDATE_INTERVAL
import time

print("=" * 45)
print("     AI Trading Signal Bot Pro")
print("=" * 45)

while True:
    try:
        price = get_live_price(SYMBOL)
        signal = get_signal(price)

        print(f"Symbol : {SYMBOL}")
        print(f"Price  : {price}")
        print(f"Signal : {signal}")
        print("-" * 45)

    except Exception as e:
        print("Error:", e)

    time.sleep(UPDATE_INTERVAL) 