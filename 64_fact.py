number = int(input('Введите целое неотрицательное число : '))
while number <1:
    number = int(input('Введите целое неотрицательное число : '))
fact = 1
for klomo in range(1, number +1):
        fact = fact * klomo
print('Факториал числа', number, 'равен', fact)
