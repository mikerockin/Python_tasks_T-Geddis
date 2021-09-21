import random
box_1 = 0
box_2 = 0
total = box_1 + box_2
x = random.randint(0,3)
print(x)
number_of_user = int(input('Угадайте случайное число от 1 до 100: '))
while number_of_user > x:
    box_1 +=1
    print('Слишком много, попробуйте еще раз')
    number_of_user = int(input('Угадайте случайное число от 1 до 100: '))
while number_of_user < x:
    box_2 +=1
    print('Слишком мало, попробуйте еще раз')
    number_of_user = int(input('Угадайте случайное число от 1 до 100: '))
while number_of_user == x:
    print('Мои поздравления, вы угадали!!!')
    print(total)
    x = random.randint(0, 3)
    print(x)
    number_of_user = int(input('Играем снова, угадайте случайное число от 1 до 100: '))



