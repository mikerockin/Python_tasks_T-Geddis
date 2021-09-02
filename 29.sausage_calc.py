import math
food_lovers = int(input('Введите количество участников хотдогового фестиваля'))
hot_dogs = int(input('Введите количество хот-догов на одного участника'))
single_sausage = 0.1
single_bun = 0.125
total_food = food_lovers * hot_dogs
pack_of_sausage_fact = total_food / 10
pack_of_bun_fact = total_food / 8
pack_of_sausage = math.ceil(total_food / 10)
pack_of_bun = math.ceil(total_food / 8)
remain_bun = round((pack_of_bun - pack_of_bun_fact) / single_bun)
remain_sausage = round((pack_of_sausage - pack_of_sausage_fact) / single_sausage)
print('Вам понадобиться:')
print('Упаковок булочек по факту: ', pack_of_bun_fact)
print('Упаковок булочек минимум: ', pack_of_bun)
print('Булочек останется: ', remain_bun)
print('Упаковок сосисок по факту: ', pack_of_sausage_fact)
print('Упаковок сосисок минимум: ', pack_of_sausage)
print('Cосисок останется: ', remain_sausage)





