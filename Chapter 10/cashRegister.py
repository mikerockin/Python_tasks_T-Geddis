# -*- coding: utf8 -*-
import ret
class CashRegister:

    # Инициализировать пустой словарь для приобретенных товаров.
    def __init__(self):

        self.__items = []

    # Очищает содержимое кассового аппарата.
    def clear(self):

        self.__items = []

    # Имитирует добавление товара в кассовый аппарат.
    # Получает объект RetailItem в качестве аргумента.
    def purchase_item(self, retail_item):

        self.__items.append(retail_item)
        print('Товар был добавлен в кассовый аппарат.')

    # Возвращает общую стоимость товаров в кассовом аппарате.
    def get_total(self):

        total = 0.0
        for item in self.__items:
            total = total + item.get_price()

        return total

    # Печатает список товаров в кассовом аппарате.
    def show_items(self):

        print('Товары в кассовом аппарате:')
        print()
        for item in self.__items:
            print(item)
            print()




