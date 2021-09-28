infile = open('number_list.txt','r')
for line in infile:
    buke = line.rstrip('\n')
    print(buke)
infile.close()
