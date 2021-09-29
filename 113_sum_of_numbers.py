def main():
    infile = open('num.txt', 'r')
    line = infile.readline()
    sum = 0
    while line != '':
        sum = sum + int(line.rstrip('\n'))
        line = infile.readline()
    print(sum)
    infile.close()
main()