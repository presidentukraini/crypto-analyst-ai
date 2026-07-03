def get_trend(last):
    if last["ema20"] > last["ema50"]:
        return "Бичачий 🟢"
    elif last["ema20"] < last["ema50"]:
        return "Ведмежий 🔴"
    else:
        return "Нейтральний ⚪"


def get_momentum(last):
    if last["macd"] > last["macd_signal"]:
        return "Бичачий 🟢"
    else:
        return "Ведмежий 🔴"