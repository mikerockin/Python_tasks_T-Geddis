print('Число\t Квадрат числа')
print('--------------------')
end = int(input('Насколько далеко мне заходить?'))
for number in range (1, end + 1):
    square = number**2
    print(number, '\t', square)


