good_cost = int(input('Введите сумму покупки: '))
per_regional_tax = 0.025
per_fed_tax = 0.05
regional_tax = good_cost * per_regional_tax
fed_tax = good_cost * per_fed_tax
all_tax = fed_tax + regional_tax
total_price = good_cost + all_tax
print('Сумма покупки: ', good_cost)
print('Общий налог с продаж: ', all_tax)
print('Итоговая сумма: ', total_price)