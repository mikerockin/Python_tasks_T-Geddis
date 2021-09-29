import random
def main():
    amount_random_numbers = int(input('Введите количество чисел, которое необходимо сгенерировать: '))
    outfile = open('random_numbers.txt', 'w')
    for line in range(1, amount_random_numbers +1):
        line = random.randint(1,500)
        outfile.write(str(line) + '\n')
    outfile.close()
main()