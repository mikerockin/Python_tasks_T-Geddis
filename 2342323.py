while name == name_user:
    print('Ваш выбор:', name_user)
    print('Выбор компьютера: ', name)
    print('Ничья, переигрываем')
    x = random.randint(1, 3)
    print(x)
    name = computer(x)
    name_user = input('Камень? Ножницы? Бумага? ')