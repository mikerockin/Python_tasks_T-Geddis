def main():
    print('Эта программа определяет является ли число простым')
    number = int(input('Введите число: '))
    prime = is_prime(number)
    if prime == False:
        print('Число', number, 'простое число')
    else:
        print('Число', number, 'простым не является (; ')
def is_prime(number):
    if number == 2 or number ==3:
        number = False
    elif number % 2 !=0 and number % 3 !=0:
        number = False
    elif number % number == 0 and number % 1 == 0:
        number= True
    return number
main()
