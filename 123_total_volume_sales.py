list_sales = []
for r in range (7):
    x = 1
    x += r
    print('Необходимо будет ввести сууму продаж для каждого дня' , x)
    sales_user = int(input('Введите сумму продаж для 7 дней подряд в $:  '))
    list_sales.append(sales_user)
print('Суммы продаж с понедельника по воскресенье:', list_sales)
total = 0
for value in list_sales:
    total += value
print('Сумма продаж за неделю составила: ', total, '$')


