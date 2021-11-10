def binary_search(my_list, item):
    my_list = [1, 3, 5, 7, 9]
    low = 0                   # в переменных low и high хранятся границы части списка в которой происходит поиск
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = my_list[mid] - 1
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None
binary_search()

