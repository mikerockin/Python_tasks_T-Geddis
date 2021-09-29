def main():
    try:
        user_file = input('Введите название файла для открытия: ')
        infile = open(user_file, 'r')
        line = infile.readline()
        sum = 0
        amount = 0
        while line != '':
            sum = sum + int(line.rstrip('\n'))
            amount += 1
            line = infile.readline()
            average_arith = sum / amount
        print(average_arith)
        infile.close()
    except IOError:
        print('Произошла ошибка при попытке прочитать файл.')
    except ValueError:
        print('В файле найдены нечисловые данные.')
main()