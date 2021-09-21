def is_prime(x):
    for x in range(1, 101):
        if x == 2:
            print('2')
        elif x == 3:
            print('3')
        elif x % x == 0 and x % 1 == 0:
            print(x)
is_prime()