# -*- coding: utf8 -*-
import ret

def main():
    goods_1 = ret.RetailItem('Пиджак', 12 , 59.95)
    goods_2 = ret.RetailItem('Дизайнерские джинсы', 40, 34.95)
    goods_3 = ret.RetailItem('Рубашка' , 20, 24.95)

    print('Товарная позиция № 1')
    print(goods_1)
    print()
    print('Товарная позиция № 2')
    print(goods_2)
    print()
    print('Товарная позиция № 3')
    print(goods_3)
    print()

main()