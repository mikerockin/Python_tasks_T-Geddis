import random
d = 0
z = 0
for x in range (100):
    x = random.randint(895, 2464)
    if x % 2 == 0:
        d = d + 1
    elif x % 2 != 0:
        z = z + 1
    print(x)
print('Количество четных чисел: ', d)
print('Количество нечетных чисел: ', z)