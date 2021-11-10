# -*- coding: utf8 -*-
class Procedure:
    def __init__(self,name, date, doc, price):
        self.__name = name
        self.__date = date
        self.__doc = doc
        self.__price = price
    def set_name(self):
        self.__name = name
    def set_date(self):
        self.__date = date
    def set_doc(self):
        self.__doc = doc
    def set_price(self):
        self.__price
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_doc(self):
        return self.__get_doc
    def get_price(self):
        return self.__price
    def __str__(self):
        return 'Название процедуры: ' + self.__name +\
            '\nДата процедуры: ' + self.__date + '\nИмя врача: ' +\
            '\nСтоимость процедуры: ' + format(self.__price, ',.2f') + '\n'
