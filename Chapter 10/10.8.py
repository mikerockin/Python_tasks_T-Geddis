# -*- coding: utf8 -*-
import ret
import cashRegister

PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

# Главный метод
def main():

    # Создать продаваемые товары.
    pants = ret.RetailItem('Брюки', 10, 19.99)
    shirt = ret.RetailItem('Рубашка', 15, 12.50)
    dress = ret.RetailItem('Платье', 3, 79.00)
    socks = ret.RetailItem('Носки', 50, 1.00)
    sweater = ret.RetailItem('Свитер', 5, 49.99)

    # Создать словарь продаваемых товаров.
    sale_items = {PANTS:pants, SHIRT:shirt,
                  DRESS:dress, SOCKS:socks,
                  SWEATER:sweater}

    # Создать кассовый аппарат.
    register = cashRegister.CashRegister()

    # Инициализировать проверку цикла.
    checkout = 'Н'

    # Пользователь хочет приобрести дополнительные товары:
    while checkout == 'Н':

        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print('Этого товара нет в наличии.')
        else:
            register.purchase_item(item)

            # Обновить товарную позицию
            new_item = ret.RetailItem(item.get_desc(), \
                                         item.get_inventory()-1, \
                                         item.get_price())
            sale_items[user_choice] = new_item

            checkout = input('Вы готовы оформить покупку (Д/Н)? ')

    print()
    print('Сумма Вашей покупки составляет: ', \
          format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()

def get_user_choice():
    print('Menu')
    print('---------------------------------')
    print('1. Брюки')
    print('2. Рубашка')
    print('3. Платье')
    print('4. Носки')
    print('5. Свитер')
    print()

    choice = int(input('Введите пункт меню товара, ' + \
                       'который вы хотели бы приобрести: '))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input('Введите допустимый номер товара: '))
        print()

    return choice

# Вызвать главную функцию.
main()




