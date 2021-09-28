def main():
    infile = open('names.txt', 'r')
    line = infile.readline()
    line_read = 0
    while line != '':
        print(line.rstrip('\n'))
        line = infile.readline()
        line_read += 1
    print(line_read)

    infile.close()

main()