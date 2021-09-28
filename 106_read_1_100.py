outfile = open('number_list.txt', 'w')
for num in range(1,101):
    outfile.write(str(num) + '\n')
outfile.close()