po = int(input('Введите количество приобретенных пакетов'))
cost = 99
total_cost = cost * po
discount_10 = 0.1
discount_20 = 0.2
discount_30 = 0.3
discount_40 = 0.4
if po >= 10 and po <= 19:
    print('Сумма скидки составила:', total_cost * discount_10, '$')
    print('Итоговая сумма:', total_cost - total_cost * discount_10, '$')
elif po >= 20 and po <= 49:
    print('Сумма скидки составила:', total_cost * discount_20, '$')
    print('Итоговая сумма:', total_cost - total_cost * discount_20, '$')
elif po >= 50 and po <= 99:
    print('Сумма скидки составила:', total_cost * discount_30, '$')
    print('Итоговая сумма:', total_cost - total_cost * discount_30, '$')
elif po >= 100:
    print('Сумма скидкb составила:', total_cost * discount_40, '$')
    print('Итоговая сумма:', total_cost - total_cost * discount_40, '$')



