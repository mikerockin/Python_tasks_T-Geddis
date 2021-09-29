def main():
    #Получить список с хранящимися в нем значениями
    numbers = get_values()
    print('Числа в списке: ')
    print(numbers)
    # Эта функция возвращает ссылку на список
def get_values():
    values = []
    # Создаем переменную для управлления циклом
    again = 'д'
    while again == 'д':
        #Получить число и добавить его в список
        num  = int(input('Введите число: '))
        values.append(num)
        #Желаете проделать это еще раз
        print('Желаете добавить еще одно число')
        again = input(('д = да, все остальное = нет: '))
        print()
    return values
main()


