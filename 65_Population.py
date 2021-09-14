start_amount_org = int(input('Введите начальное количество организмов: '))
amount_days = int(input('Введите количество дней на размножение организмов: '))
average_day_pop = int(input('Введите среднесуточное увеличение популяции в процентах: '))/100
print('День\tПопуляция')
print('_______________')
for x in range (1, amount_days +1):
    print(x, '\t', format(start_amount_org, '.3f'))
    start_amount_org = start_amount_org * average_day_pop + start_amount_org
print()
