BASE_YEAR= 1903
def main():
    infile = open('WorldSeriesWinners.txt', 'r')
    results = infile.readline()
    print(results)
main()