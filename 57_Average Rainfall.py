years = int(input('Введите количество лет : '))
print('Введите количество осадков в каждом месяце начиная с января.. ')
month_pre = 0
for y in range(1, years+1):
    for x in range(1, 13):
        precipitation = int(input('Введите кол-осадков в мм : '))
        month_pre += precipitation
months =  years * 12
print("Общее количество месяцев : ", months, '\t', "Общее количество осадков в мм : ", month_pre)
print('Среднее количество осадков в месяц в мм : ', month_pre / months)
