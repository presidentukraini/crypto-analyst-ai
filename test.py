def generate_summary(trend, momentum, rsi):


 if trend == "Ведмежий 🔴" and momentum == "Ведмежий 🔴":
    summary = "SHORT має перевагу, тому що тренд і імпульс підтверджують спад."
elif trend == "Ведмежий 🔴" and momentum == "Бичачий 🟢":
    summary = "Є конфлікт між трендом та імпульсом. Краще чекати."
elif trend == "Бичачий 🟢" and momentum == "Бичачий 🟢":
    sumarry = "LONG має перевагу, тренд підтверджений."

    return summary;