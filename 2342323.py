def main():
    infile = open('names.txt', 'r')
    line = infile.readline()
    line_read = 0
    while line != '':
        line_read +=1
        print(line)
        line = infile.readline()


    infile.close()
main()