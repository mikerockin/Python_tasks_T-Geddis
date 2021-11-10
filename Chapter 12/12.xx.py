# -*- coding: utf8 -*-

def main():
    message(5)

def message(times):
    if times > 0:
        print('Это рекурсивная функция')
        message(times-1)
main()