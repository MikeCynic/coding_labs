salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
costs=0
earnings=0
for i in range(months):
    earnings += salary
    costs += spend
    spend *= (increase+1)
m = costs - earnings
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(m))
