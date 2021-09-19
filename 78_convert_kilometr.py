def main():
    km = int(input('Ведите расстояние в километрах: '))
    kmmiles = miles(km)
    print(kmmiles)
def miles(km):
    mil = km * 0.6214
    return mil
main()