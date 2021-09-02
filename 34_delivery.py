weight = int(input('Введите массу груза в граммах, для расчета стоимости доставки'))
cf_1 = 1.5
cf_2 = 3.0
cf_3 = 4.4
cf_4 = 4.75
if weight < 100:
    print('Стоимость доставки составит: ', 100 * cf_1, 'RUB')
elif weight <= 200:
    print('Стоимость доставки составит: ', weight * cf_1, 'RUB')
elif weight > 200 and weight <= 600:
    print('Стоимость доставки составит: ', weight * cf_2, 'RUB')
elif weight > 600 and weight <= 1000:
    print('Стоимость доставки составит: ', weight * cf_3, 'RUB')
elif weight > 1000:
    print('Стоимость доставки составит: ', weight * cf_4, 'RUB')

