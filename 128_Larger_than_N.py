list = [2, 3, 5, 6, 45]
n = 4
def main():
    larger_than_N = compare(list, n)
def compare (list, n):
    for x in list:
        if n < x:
            print(x)
main()