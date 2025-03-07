answer = 'да'
while answer == 'да':
    a = int(input('Введите число: '))
    b = int(input('Введите еще одно: '))
    total = a + b
    print(total)
    answer = input('Желаете ли вы выполнить операцию еще раз?')
