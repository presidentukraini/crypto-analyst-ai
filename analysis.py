from strategy import get_trend, get_momentum
from score import calculate_score, get_signal_strength
from config import RSI_OVERBOUGHT, RSI_OVERSOLD

def generate_summary(trend, momentum, rsi):
    if trend == "Ведмежий 🔴" and momentum == "Ведмежий 🔴":
        summary = "SHORT має перевагу, тому що тренд і імпульс підтверджують спад."
    elif trend == "Ведмежий 🔴" and momentum == "Бичачий 🟢":
        summary = "Є конфлікт між трендом та імпульсом. Краще чекати."
    elif trend == "Бичачий 🟢" and momentum == "Бичачий 🟢":
        summary = "LONG має перевагу, тренд підтверджений."
    elif trend == "Бичачий 🟢" and momentum == "Ведмежий 🔴":
        summary = "Є конфлікт: тренд вгору, але імпульс слабшає. Краще чекати."
    else:
        summary = "Ситуація нечітка. Краще чекати."
    if rsi > RSI_OVERBOUGHT:
        summary += " Але RSI показує перекупленість, тому входити в LONG ризиковано."
    elif rsi < 30:
        summary += " Але RSI показує перепроданість, тому входити в SHORT ризиковано."

    return summary

def analyze_market(df):
    last = df.iloc[-1]

    trend = get_trend(last)
    momentum = get_momentum(last)

    long_score, short_score = calculate_score(
    rsi=last["rsi"],
    trend=trend,
    momentum=momentum,
    volume=last["volume"],
    volume_avg=last["volume_avg"],
    adx=last["adx"]
)

    side, score, strength = get_signal_strength(long_score, short_score)
    
    summary = generate_summary(
    trend,
    momentum,
    last["rsi"]
)
    analysis = {
        "price": last["close"],
        "rsi": round(last["rsi"], 2),
        "ema20": round(last["ema20"], 2),
        "ema50": round(last["ema50"], 2),
        "macd": round(last["macd"], 2),
        "macd_signal": round(last["macd_signal"], 2),
        "trend": trend,
        "adx": round(last["adx"], 2),
        "summary": summary,
        "momentum": momentum,
        "long_score": long_score,
        "short_score": short_score,
        "side": side,
        "score": score,
        "strength": strength,
        "volume": round(last["volume"], 2),
        "volume_avg": round(last["volume_avg"], 2),
    }

    return analysis