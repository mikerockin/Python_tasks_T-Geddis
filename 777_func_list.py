def main():
    numbers = [2, 4, 6, 8, 10]
    print('Сумма составляет', get_total(numbers))
def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total
main()