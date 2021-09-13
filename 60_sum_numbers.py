print('Сейчас как начнем вводить положительные цифры')
numbers = 0
sum_numbers = 0
while numbers >= 0:
    sum_numbers += numbers
    numbers = int(input('Введите положительное число, для завершения работы введите отрицательное число '))
print(sum_numbers)

