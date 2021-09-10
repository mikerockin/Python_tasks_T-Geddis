years = int(input('Введите количество лет : '))
months = 12
precipitation_all = 0
call = 1
print('Введите количество осадков в каждом месяце начиная с января.. ')
print('№ месяца\tКоличество осадков')
print('____________________________')
for x in range(years):
    for b in range(1, months + 1):
        precipitation = int(input('Введите кол-осадков в мм : '))
        precipitation_all += precipitation
        print(precipitation_all)
        print(b, '\t', precipitation_all)


