# -*- coding: utf8 -*-

def main():

    num1 = 0

    while num1 <= 0:
        num1 = int(input('Введите число номер 1: '))
    num2 = 0

    while num2 <= 0:
        num2 = int(input('Введите число номер 2: '))

    print(num1, 'умножить на', num2, 'Равно', func(num1,num2))

def func(x,y):
    if x == 0 or y ==0:
        return 0
    else:
        return x + func(x, y -1)
main()

