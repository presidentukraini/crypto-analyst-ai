from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD, ADXIndicator
from config import EMA_FAST, EMA_SLOW


def add_indicators(df):
    rsi_indicator = RSIIndicator(close=df["close"], window=14)
    df["rsi"] = rsi_indicator.rsi()

    ema_fast_indicator = EMAIndicator(close=df["close"], window=EMA_FAST)
    ema_slow_indicator = EMAIndicator(close=df["close"], window=EMA_SLOW)

    df["ema20"] = ema_fast_indicator.ema_indicator()
    df["ema50"] = ema_slow_indicator.ema_indicator()

    macd_indicator = MACD(close=df["close"])
    df["macd"] = macd_indicator.macd()
    adx_indicator = ADXIndicator(
    high=df["high"],
    low=df["low"],
    close=df["close"]
    )

    df["adx"] = adx_indicator.adx()
    df["volume_avg"] = df["volume"].rolling(window=20).mean()
    df["macd_signal"] = macd_indicator.macd_signal()

    return df