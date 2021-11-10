# -*- coding: utf8 -*-
def main():

    number_list = [1, 2, 3, 4, 5, 6, 15, 8, 9, 10]

    print('Список чисел:\n', number_list, sep='')

    print('Максимальное число в списке: ', find_largest(number_list))

def find_largest(numlist):
    n = len(numlist)
    if n == 1:
        return numlist[0]
    else:
        temp = find_largest(numlist[0:n-1])
        if numlist[n-1] > temp:
            return numlist[n-1]
        else:
            return temp

main()
