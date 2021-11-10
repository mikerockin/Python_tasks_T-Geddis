# -*- coding: utf8 -*-
# Упражнение по программированию 12-6

# Сумма чисел

def main():
    # Локальная переменная
    num = 0

    # Получить от пользователя число.
    while num <= 0:
        num = int(input('Введите целое положительное число: '))

    # Вызвать функцию sum_num и показать сумму.
    print('Сумма от 1 до', num, 'равняется', format(sum_nums(num), ','))

# Функция sum_nums принимает целочисленный аргумент и возвращает
# сумму всех целых чисел, начиная с 1 до числа, переданного в
# качестве аргумента.
def sum_nums(n):
    if n == 0:
        return n
    else:
        return n + sum_nums(n-1)

# Вызвать главную функцию.
main()
