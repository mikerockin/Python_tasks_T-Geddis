# Упражнение по программированию 7-12

# Генерация простого числа

# Функция prime_or_composite принимает целое число и
# показывает сообщение о том, является ли полученное значение
# простым или составным числом.

def prime_or_composite(n):
    has_divisor = False

    for i in range(2, n):
        if n % i == 0:
            has_divisor = True

    if has_divisor:
        print(n, 'является составным.')
    else:
        print(n, 'является простым.')


def main():
    # Получить от пользователя целое число.
    user_num = int(input('Введите целое число больше 1: '))

    # Создать пустой список.
    numbers = []

    # Заполнить список числами.
    for count in range(2, user_num + 1):
        numbers.append(count)

    # Определить, является ли каждый элемент простым или составным.
    for i in range(len(numbers)):
        prime_or_composite(numbers[i])


# Вызвать главную функцию
main()
