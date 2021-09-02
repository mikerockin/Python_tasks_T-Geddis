pocket = int(input('Введите номер кармана'))
if pocket == 0:
    print('Зеленый')
elif pocket >= 1 and pocket <= 10 and pocket % 2 == 1:
    print('Красный')
elif pocket >= 1 and pocket <= 10 and pocket % 2 != 1:
    print('Черный')
elif pocket >= 11 and pocket <= 18 and pocket % 2 == 1:
    print('Черный')
elif pocket >= 11 and pocket <= 18 and pocket % 2 != 1:
    print('Красный')
elif pocket >= 19 and pocket <= 28 and pocket % 2 == 1:
    print('Красный')
elif pocket >= 19 and pocket <= 28 and pocket % 2 != 1:
    print('Черный')
elif pocket >= 29 and pocket <= 36 and pocket % 2 == 1:
    print('Красный')
elif pocket >= 29 and pocket <= 36 and pocket % 2 != 1:
    print('Черный')
else:
    print('Error, the pocket is not in 0 ....36 ')
