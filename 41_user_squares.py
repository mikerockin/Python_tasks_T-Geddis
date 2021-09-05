print('Число\t Квадрат числа')
print('--------------------')
start = int(input('Введите начальное число:'))
end = int(input('Насколько далеко мне заходить?'))
for number in range (start, end + 1):
    square = number**2
    print(number, '\t', square)