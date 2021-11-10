# -*- coding: utf8 -*-

def main():

   number = 0
   number = int(input('Сколько строк показать? '))
   lines(number)

def lines(n):
    if n > 1:
        lines(n - 1)
    for i in range(n):
        print('*', end='')
    print()

main()