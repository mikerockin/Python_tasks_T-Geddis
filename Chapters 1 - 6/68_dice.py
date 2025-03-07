import random

MIN = 1
MAX = 6

def main():
    again = 'д'
    while again == 'д' or again == 'Д':
        print('Бросаем кубики...')
        print('Значение граней: ')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        again = input('Бросить кубики еще раз (д = да):')
main()