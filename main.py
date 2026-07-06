from market_data import get_live_price
import time

print("=" * 45)
print(" AI Trading Signal Bot Pro")
print("=" * 45)

while True:
    try:
            price = get_live_price("BTCUSDT")
                    print(f"Live Price: {price}")
                        except Exception as e:
                                print("Error:", e)

                                    time.sleep(5)