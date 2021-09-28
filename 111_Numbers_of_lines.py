def main():
    filename = input('Введите имя файла для открытия: ')
    infile = open(filename, 'r')
    line = infile.readline()
    line_number = 0
    while line != '':
        line_number += 1
        print(str(line_number) + ':', line.rstrip('\n'))
        line = infile.readline()

    infile.close()

main()
