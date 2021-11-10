# -*- coding: utf8 -*-

def main():
    number = 0
    number = int(input('Какое количество цифр показать?'))
    print_num(number)

def print_num(n):
    if n > 1:
        print_num(n-1)
    print(n)
main()