def main():
    numbers = [1,2,3,4]
    sum = get_total(numbers)
    print(sum)
def get_total(sum):
    total = 0
    for x in sum:
        total += x
    return  total
main()
