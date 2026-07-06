def get_signal(price):
        if price > 60000:
                return "BUY"
                    elif price < 59000:
                            return "SELL"
                                else:
                                        return "WAIT"