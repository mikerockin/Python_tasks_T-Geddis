def main():
    max_line_to_read = 5
    lines_read = 0
    filename = input('Введите имя файла для открытия: ')
    infile = open(filename, 'r')
    line = infile.readline()
    lines_read += 1
    while line != '' and lines_read <= max_line_to_read:
        print(line.rstrip('\n'))
        line = infile.readline()
        lines_read += 1


    infile.close()

main()

