print('№ месяца\tКоличество осадков')
print('____________________________')
years = int(input('Введите количество лет : '))
months = 12
precipitation_all = 0
print('Введите количество осадков в каждом месяце начиная с января.. ')
for x in range(years):

    for b in range(1, months + 1):
        print(b, '\t', drop)
        precipitation = int(input('Введите кол-осадков в мм : '))
        precipitation_all += precipitation
        drop = precipitation_all * 1