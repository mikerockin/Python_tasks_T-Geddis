def main ():
    number = int(input('Введите число: '))
    result = times_ten(number)
    print(result)
def times_ten(number):
    result = number * 10
    return result
main()