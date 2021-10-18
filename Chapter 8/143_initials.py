def main():
    full_name = input('Введите свое полное имя: ')
    name = full_name.split()
    for string in name:
        print(string[0].upper(),sep='', end='')
        print('.', sep=' ', end='')
main()

