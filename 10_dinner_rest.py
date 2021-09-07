food_price = int(input('Введите стоимость жратвы: '))
per_tips = 0.18
per_tax_sales = 0.07
tips = food_price * per_tips
tax_sales = int(food_price * per_tax_sales)
cost_with_tips = food_price + tips
cost_with_tax = food_price + tax_sales
total_cost = food_price + tips + tax_sales
print('Cумма на еду составила: ', food_price)
print('Сумма налога с продаж: ', tax_sales )
print('Сумма чаевых: ', tips)
print('Стоимость еды плюс налог с продаж: ', cost_with_tax)
print('Стоимость еды плюс чаевые: ', cost_with_tips)
print('Итоговая сумма составила: ', total_cost)

