import schedule
import time
import subprocess


def run_scanner():
    print("Запускаю сканер...")
    subprocess.run(["python", "scanner.py"])


schedule.every(5).minutes.do(run_scanner)

print("Crypto Analyst AI працює в авто-режимі.")
print("Сканування кожні 5 хвилин.")
print("Щоб зупинити — натисни Ctrl + C.")

run_scanner()

while True:
    schedule.run_pending()
    time.sleep(1)