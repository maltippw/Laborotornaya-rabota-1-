salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0
while months > 0:
    money_capital += spend - salary
    spend *= 1 + increase
    months -= 1
print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", round(money_capital))
