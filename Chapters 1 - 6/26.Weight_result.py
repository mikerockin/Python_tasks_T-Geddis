weight = int(input('Введите массу тела в ньютонах'))
heft = format(weight * 9.8, ',.2f')
if weight > 500:
    print('Тело слишком тяжелое')
elif weight < 100:
    print('Тело слишком легкое')
else:
    print('Полученный вес:', heft)
