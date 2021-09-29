def main():
    infile = open('random_numbers.txt', 'r')
    line = infile.readline()
    sum = 0
    amount = 0
    while line != '':
        sum = sum + int(line.rstrip('\n'))
        amount += 1
        line = infile.readline()
        print(line.rstrip('\n'))
    print('Сумма полученных чисел равна: ',sum)
    print('Количество считанных чисел равно:' , amount)
    infile.close()
main()