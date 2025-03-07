level_cof = 1.6
print('Years\tlevel oc')
print('_____________')
for x in range (1, 25):
    level_oc = x * level_cof
    print(x, '\t',format(level_oc, ',.2f'))