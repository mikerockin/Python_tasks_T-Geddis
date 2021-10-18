def main():
    user_numbers = input('Введите многоразрядное число: ')
    total = string_total(user_numbers)
    print('Сумма введенных чисел равна', total)
def string_total(user_numbers):
    number = 0
    total = 0
    for i in range(len(user_numbers)):
        number = int(user_numbers[i])
        total += number
    return total
main()
