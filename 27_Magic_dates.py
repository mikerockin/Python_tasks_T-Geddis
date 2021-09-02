months = int(input('Введите порядковый номер месяца'))
days = int(input('Введите порядковый номер дня'))
years = int(input('Введите год в двух разрядном виде, например: 1988 = 88'))
if months * days == years:
    print('Это волшебная дата')
else:
    print('Эта дата не волшебная!')

if color1 != 'red' and color1 != 'blue' and color1 != 'yellow':
    print('Неверный цвет ')
elif color1 == 'red' and color2 == 'blue' and color2 == 'red' and color1 == 'blue':
    print('Фиолетовый')
elif color2 != 'red' and color2 != 'blue' and color2 != 'yellow':
    print('Неверный цвет ')