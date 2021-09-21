def main():
    print('Данная программа показывает максимальное значение из двух введенных')
    value_1 = int(input('Введите число: '))
    value_2 = int(input('Введите еще одно число: '))
    max_from_two = max(value_1, value_2)
    print(max_from_two)
def max(x,y):
    if x > y:
        return x
    else:
        return y
main()

