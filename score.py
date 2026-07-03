from weights import TREND_WEIGHT, MOMENTUM_WEIGHT, RSI_WEIGHT, VOLUME_WEIGHT, ADX_WEIGHT


def calculate_rsi_score(rsi):
    long_score = 0
    short_score = 0

    if rsi < 30:
        long_score += RSI_WEIGHT
    elif rsi > 70:
        short_score += RSI_WEIGHT

    return long_score, short_score


def calculate_trend_score(trend):
    long_score = 0
    short_score = 0

    if trend == "Бичачий 🟢":
        long_score += TREND_WEIGHT
    elif trend == "Ведмежий 🔴":
        short_score += TREND_WEIGHT

    return long_score, short_score


def calculate_momentum_score(momentum):
    long_score = 0
    short_score = 0

    if momentum == "Бичачий 🟢":
        long_score += MOMENTUM_WEIGHT
    elif momentum == "Ведмежий 🔴":
        short_score += MOMENTUM_WEIGHT

    return long_score, short_score


def calculate_volume_score(volume, volume_avg, trend):
    long_score = 0
    short_score = 0

    if volume > volume_avg:
        if trend == "Бичачий 🟢":
            long_score += VOLUME_WEIGHT
        elif trend == "Ведмежий 🔴":
            short_score += VOLUME_WEIGHT

    return long_score, short_score


def calculate_adx_score(adx, trend):
    long_score = 0
    short_score = 0

    if adx > 25:
        if trend == "Бичачий 🟢":
            long_score += ADX_WEIGHT
        elif trend == "Ведмежий 🔴":
            short_score += ADX_WEIGHT

    return long_score, short_score


def calculate_score(rsi, trend, momentum, volume, volume_avg, adx):
    long_score = 0
    short_score = 0

    rsi_long, rsi_short = calculate_rsi_score(rsi)
    trend_long, trend_short = calculate_trend_score(trend)
    momentum_long, momentum_short = calculate_momentum_score(momentum)
    volume_long, volume_short = calculate_volume_score(volume, volume_avg, trend)
    adx_long, adx_short = calculate_adx_score(adx, trend)

    long_score += rsi_long + trend_long + momentum_long + volume_long + adx_long
    short_score += rsi_short + trend_short + momentum_short + volume_short + adx_short

    return long_score, short_score


def get_signal_strength(long_score, short_score):
    if long_score > short_score:
        side = "LONG"
        score = long_score
    elif short_score > long_score:
        side = "SHORT"
        score = short_score
    else:
        side = "WAIT"
        score = long_score

    if score < 40:
        side = "WAIT"
        strength = "Чекати"
    elif score < 65:
        strength = "Слабка перевага"
    elif score < 85:
        strength = "Сильна перевага"
    else:
        strength = "Дуже сильний сигнал"

    return side, score, strength