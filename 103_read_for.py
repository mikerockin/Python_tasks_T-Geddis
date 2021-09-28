infile = open('number.txt', 'r')
for line in infile:
    bike = line.rstrip('\n')
    print(bike)
infile.close()