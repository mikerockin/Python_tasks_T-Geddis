import random
def main():
    x = random.randint(1, 3)
    print(x)
    name = computer(x)
    name_user = input('Камень? Ножницы? Бумага? ')
    compare_com = compare(name, name_user)
def computer(x):
    if x == 1:
       name = 'Камень'
    elif x == 2:
       name = 'Ножницы'
    elif x == 3:
       name = 'Бумага'
    return name
def compare(com, user):
    if com == 'Камень' and user == 'Ножницы':
        print('Вы проиграли, камень разбивает ножницы')
    elif com == 'Ножницы' and user == 'Бумага':
        print('Вы проиграли, ножницы режут бумагу')
    elif com == 'Бумага' and user == 'Камень':
        print('Вы проиграли,бумага заворачивает камень')
    elif com == user:
        print('Ничья, переигрываем')
        print('Ваш выбор: ',user)
        print('Выбор компьютера: ', com)
        main()
    else:
        print('Вы выиграли!')
main()
