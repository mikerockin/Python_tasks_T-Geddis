AMOUNT_NUMBERS = 20
def main():
    list_number = []
    list_number = get_numbers(list_number)
    amount = len(list_number)
    min = min_number(list_number)
    max = max_number(list_number)
    total_numbers = calculate_total_numbers(list_number)
    average = calculate_average_total(total_numbers, amount)
    print('Ваша цифровая последовательность: ', list_number)
    print('Наименьшее число в последовательности: ', min)
    print('Наибольшее число в последовательности: ', max)
    print('Сумма чисел в пооследовательности: ', total_numbers)
    print('Среднее арифметивечское всей последовательности:', average)
def get_numbers(list_numbers):
    for x in range (AMOUNT_NUMBERS):
        user_numbers = int(input('Введите поочередно числовой ряд из 20 чисел: '))
        list_numbers.append(user_numbers)
    return list_numbers
def min_number (list_numbers):
    min_number = min(list_numbers)
    return min_number
def max_number (list_numbers):
    max_number = max(list_numbers)
    return max_number
def calculate_total_numbers (list_numbers):
    total = 0
    for values in list_numbers:
        total += values
    return total
def calculate_average_total (total_numbers, amount):
    average = total_numbers / amount
    return average
main()
