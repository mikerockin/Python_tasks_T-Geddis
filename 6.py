good_1 = int(input('Введите цену первого товара: '))
good_2 = int(input('Введите цену второго товара: '))
good_3 = int(input('Введите цену третьего товара: '))
good_4 = int(input('Введите цену четвертого товара: '))
good_5 = int(input('Введите цену пятого товара: '))
per_nalog = 0.07
good_all = good_1 + good_2 + good_3 + good_4 + good_5
nalog = int(good_all * per_nalog)
total_price = good_all + nalog
print('Выбарнные товары на сумму: ', good_all)
print('Итоговая сумма составляет', total_price, 'рублей', 'в том числе сумма налога: ',nalog, 'рубль')

