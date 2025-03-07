m = int(input('Enter your weight : '))
minus_m = 1.5
print('Months\tWeight')
print('_____________')
for x in range(1,7):
    m -= minus_m
    print(x, '\t', m)

