# -*- coding: utf8 -*-
class RetailItem:
    def __init__(self, desc, inventory, price):
        self.__desc = desc
        self.__inventory = inventory
        self.__price = price
    def set_desc(self):
        self.__desc = desc
    def set_inventory(self):
        self.__inventory = inventory
    def set_price(self):
        self.__price = price
    def get_desc(self):
        return self.__desc
    def get_inventory(self):
        return self.__inventory
    def get_price(self):
        return self.__price
    def __str__(self):
        result = 'Описание: ' + self.get_desc() + '\n' +\
            'Единиц на складе: ' + str(self.get_inventory()) +\
            '\nЦена: ' + str(self.get_price())
        return result

