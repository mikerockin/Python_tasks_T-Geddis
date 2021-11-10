def main():
    item = 4
    my_list = [1, 2, 3, 4, 5,]
    binary_search(my_list, item)
    print(my_list[(binary_search(my_list, item))])
def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = my_list[mid]
        if guess == item:
            return mid

        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None
main()

