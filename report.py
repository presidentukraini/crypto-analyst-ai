def print_report(data):

    print("=" * 40)
    print("CRYPTO ANALYST AI")
    print("=" * 40)

    print(f"\nПара: {data['symbol']}")
    print(f"Ціна: {data['price']}")

    print("\n----------------")

    print(f"Тренд: {data['trend']}")
    print(f"Імпульс: {data['momentum']}")

    print(f"RSI: {data['rsi']}")
    print(f"Обʼєм: {data['volume']}")
    print(f"Середній обʼєм: {data['volume_avg']}")
    print(f"EMA20: {data['ema20']}")
    print(f"EMA50: {data['ema50']}")

    print(f"MACD: {data['macd']}")
    print(f"Signal: {data['macd_signal']}")
    print(f"ADX: {data['adx']}")

    print("\n----------------")

    print(f"LONG: {data['long_score']}/100")
    print(f"SHORT: {data['short_score']}/100")

    print(f"\nРішення: {data['side']}")
    print(f"Оцінка: {data['score']}/100")
    print(f"Сила сигналу: {data['strength']}")

    print("\nВисновок:")
    print(data["summary"])