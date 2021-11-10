# -*- coding: utf8 -*-
class Employee:
    def __init__(self, name, id_number, dep, position):
        self.__name = name
        self.__id_number = id_number
        self.__dep = dep
        self.__position = position
    def set_name(self):
        self.__name = name
    def set_id(self):
        self.__id = id_number
    def set_dep(self):
        self.__dep = dep
    def set_position(self):
        self.__position = position
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_dep(self):
        return self.__dep
    def get_position(self):
        return self.__position
    def __str__(self):
        result = 'Имя: ' + self.get_name() +\
            '\nИдентификационный номер: ' + self.get_id_number() +\
            '\nОтдел: ' + self.get_dep() +\
            '\nДолжность: ' + self.get_position()
        return result
