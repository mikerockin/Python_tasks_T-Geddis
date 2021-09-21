import random
x = random.randint(100, 300)
y = random.randint(150, 400)
print(x)
print(y)
total = int(input('Введите чему равна сумма: '))
if total == x + y:
    print('Поздравляем, ответ верный!')
else:
    print('Сумма чисел равна: ', x + y)