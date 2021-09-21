import random
def main():
    x = random.randint(1, 3)
    name = computer(x)
    name_user = input('Камень? Ножницы? Бумага? ')
    print('Ваш выбор:', name_user)
    print('Выбор компьютера', name)
def computer(x):
    if x == 1:
       name = 'Камень'
    elif x == 2:
       name = 'Ножницы'
    elif x == 3:
       name = 'Бумага'
    return name
main()
