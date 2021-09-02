year = int(input('Введите год в формате хххх'))
if year % 100 ==0 and year % 400 ==0:
    print('Дней в феврале 29')
elif year % 100 ==0 or year % 4 ==0:
    print('Дней в феврале 29')
else:
    print('Год не високосный')