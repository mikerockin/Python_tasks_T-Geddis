years = int(input('Введите количество лет : '))
months = 12
precipitation_all = 0
print('Введите количество осадков в каждом месяце начиная с января.... ')
for x in range(years):
    for b in range(months):
        precipitation = int(input('Введите кол-осадков в мм : '))
        precipitation_all += precipitation
        print(precipitation_all)
        print(months)
