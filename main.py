from binance_api import get_market_data
from indicators import add_indicators
from analysis import analyze_market
from report import print_report
from config import DEFAULT_SYMBOL


symbol = input(f"Введи монету або натисни Enter для {DEFAULT_SYMBOL}: ")

if symbol == "":
   symbol = DEFAULT_SYMBOL

df = get_market_data(symbol)
df = add_indicators(df)

analysis = analyze_market(df)
analysis["symbol"] = symbol

print_report(analysis)