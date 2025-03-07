print('Temp С\tTemp F')
print('______________')
for x in range (0, 21):
    farengeith = (9 / 5 * x + 32)
    print(x, '\t', format(farengeith, ',.2f'))