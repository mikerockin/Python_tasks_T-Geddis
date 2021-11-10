# -*- coding: utf8 -*-
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    def __str__(self):
        return 'Имя домашнего животного: ' + self.__name +\
            'Тип домашнего животного: ' + self.__animal_type + \
            'Возраст: ' + self.__age
