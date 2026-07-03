from binance_api import get_market_data
from indicators import add_indicators
from analysis import analyze_market
from config import SYMBOLS
from telegram_bot import send_telegram_message
from datetime import datetime
from signal_memory import should_send_signal

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

results = []

for symbol in SYMBOLS:
    df = get_market_data(symbol)
    df = add_indicators(df)

    analysis = analyze_market(df)
    analysis["symbol"] = symbol
    results.append(analysis)



results.sort(
    key=lambda result: result["score"],
    reverse=True
)  





print(CYAN + "╔══════════════════════════════════════════════╗")
print("║        ⚡ CRYPTO MARKET SCANNER v1.0 ⚡       ║")
print("╚══════════════════════════════════════════════╝" + RESET)

print(f"Оновлено: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Проскановано монет: {len(results)}")
print("-" * 55)

print(f"{'#':<3} {'Монета':<10} {'Сигнал':<8} {'Бал':<5} Статус")
print("-" * 55)

for index, result in enumerate(results, start=1):
    if result["side"] == "LONG":
        color = GREEN
    elif result["side"] == "SHORT":
        color = RED
    else:
        color = YELLOW

    print(
        color +
        f"{index:<3} "
        f"{result['symbol']:<10} "
        f"{result['side']:<8} "
        f"{result['score']:<5} "
        f"{result['strength']}" +
        RESET
    )

best = results[0]

message = "🚀 CRYPTO MARKET SCANNER\n\n"

for result in results:

    if result["score"] >= 80 and should_send_signal(
        result["symbol"],
        result["side"],
        result["score"]
    ):

        message += (
    f"🟢 {result['symbol']}\n"
    f"📈 Сигнал: {result['side']}\n"
    f"⭐ Оцінка: {result['score']}/100\n"
    f"📊 Сила: {result['strength']}\n"
    f"RSI: {result['rsi']}\n"
    f"ADX: {result['adx']}\n"
    f"Volume: {result['volume']} / Avg: {result['volume_avg']}\n"
    f"Висновок: {result['summary']}\n"
    f"────────────────────\n\n"
)


if message != "🚀 CRYPTO MARKET SCANNER\n\n":
    send_telegram_message(message)

print(GREEN + "\n╔════════════ TOP SIGNAL ════════════╗")
print(f"  {best['symbol']} | {best['side']} | {best['score']}/100")
print(f"  {best['strength']}")
print("╚════════════════════════════════════╝" + RESET)