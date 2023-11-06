money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
while True: # TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
    remain = spend - salary
    if remain > money_capital:
        break
    month += 1
    money_capital -= remain
    spend *= (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", month)
