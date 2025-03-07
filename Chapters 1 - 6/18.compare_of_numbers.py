amount_1 = int(input('Введите число: '))
amount_2 = int(input('Введите еще одно число: '))
if amount_1 > 10 and amount_2 < 100:
    if amount_1 > amount_2:
        print(amount_1)
    if amount_2 > amount_1:
        print(amount_2)