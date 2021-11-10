# -*- coding: utf8 -*-
class Patient:
    def __init__(self, first, second, last, address, city, state, zip_code, phone, em_contact, em_phone):
        self.__first = first
        self.__second = second
        self.__last = last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__em_contact = em_contact
        self.__em_phone = em_phone
    def set_first(self):
        self.__first = first
    def set_second(self):
        self.__second = second
    def set_last(self):
        self.__last = last
    def set_address(self):
        self.__address = address
    def set_city(self):
        self.__city = city
    def set_state(self):
        self.__state = state
    def set_zip_code(self):
        self.__zip_code = zip_code
    def set_phone(self):
        self.__phone = phone
    def set_em_contact(self):
        self.__em_contact = em_contact
    def set_em_phone(self):
        self.__em_phone = em_phone

    def get_first(self):
        return self.__first
    def get_second(self):
        return self.__second
    def get_last(self):
        return self.__last
    def get_address(self):
        return self.__address
    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state
    def get_zip_code(self):
        return self.__zip_code
    def get_phone(self):
        return self.__phone
    def get_em_contact(self):
        return self.__em_contact
    def get_em_phone(self):
        return self.__em_phone

    def __str__(self):
        return 'Имя: ' + self.__first + '\nОтчество: ' + self.__second +\
            '\nФамилия: ' + self.__last + '\n Адрес: ' + self.__address +\
            '\nГород: ' + self.__city + '\nОбласть: ' + self.__state +\
            '\nИндекс: ' + self.__zip_code + '\nТелефонный номер: ' + \
            '\nИмя человека для экстренной связи: ' + self.__em_contact +\
            '\nНомер телефона для экстренной связи: ' + self.__em_phone + '\n'


