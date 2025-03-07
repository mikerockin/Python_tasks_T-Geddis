def main():
    print('Сейчас мы передадим аргумент из одной функции в другую')
    times_den(2)
def times_den(number):
    result = number * 10
    print(result)
main()