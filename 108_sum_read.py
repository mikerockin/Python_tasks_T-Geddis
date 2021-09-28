def main():
    infile = open('number_list.txt', 'r')
    total = 0
    for line in infile:
        sum = float(line)
        total += sum
    print(total)
    infile.close()
main()