def main():
    infile = open('num.txt', 'r')
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
main()