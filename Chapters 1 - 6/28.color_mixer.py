color1 = input('Введите цвет:')
color2 = input('Введите еще один цвет:')
if color1 == 'red' and color2 == 'blue':
    print('Фиолетовый')
elif color2 == 'red' and color1 == 'blue':
    print('Фиолетовый')
elif color2 == 'red' and color1 == 'yellow':
    print('Оранжевый')
elif color1 == 'red' and color2 == 'yellow':
    print('Оранжевый')
elif color2 == 'blue' and color1 == 'yellow':
    print('Зеленый')
elif color1 == 'blue' and color2 == 'yellow':
    print('Зеленый')
else:
    print('Error color')



food_lovers = int(input('Введите количество участников фестиваля не здоровой пищи'))
hot_dogs = int(input('Введите количество хот-догов на одного участника'))
total_food = food_lovers * hot_dogs
pack_of_sausage = total_food / 10
pack_of_bun = total_food / 8
pos_pack_saus = pack_of_sausage % 1
pos_pack_bun = pack_of_bun % 1
remainder_bun = format((1 - (pack_of_bun % 1)) / 0.125, ',.1f')
remainder_sausage = format((1 - pos_pack_saus) / 0.1, ',.1f')
if pos_pack_saus == 0:
    remainder_sausage = 0
elif pos_pack_bun == 0:
    remainder_bun = 0
print('Вам понадобиться:')
print('Упаковок булочек: ', pack_of_bun)
print('Упаковок сосисок: ', pack_of_sausage)
print('Cосисок осталось: ', remainder_sausage)
print('Булочек осталось: ', remainder_bun)
print(pos_pack_saus)
print(pos_pack_bun)