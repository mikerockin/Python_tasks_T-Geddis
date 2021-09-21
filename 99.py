import random
def main():
    box_1 = 0
    box_2 = 0
    total_box = box_1 + box_2
    x = random.randint(0, 3)
    number_of_user = int(input('Угадайте случайное число от 1 до 100: '))
    total = user_number(x, number_of_user)
    print(total_box)
def user_number(x, number):
    while number > x:
        box_1 +=1
    return box_1
main()





