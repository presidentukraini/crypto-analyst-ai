import json
import os


MEMORY_FILE = "signal_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, ensure_ascii=False, indent=4)


def should_send_signal(symbol, side, score):
    memory = load_memory()

    old_signal = memory.get(symbol)

    new_signal = {
        "side": side,
        "score": score
    }

    if old_signal == new_signal:
        return False

    memory[symbol] = new_signal
    save_memory(memory)

    return True