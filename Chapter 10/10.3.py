# -*- coding: utf8 -*-
import information

def main():

    my_info = information.Information('Джон Доу','111 Моя улица', \
                               22, '555-555-1281')
    mom_info = information.Information('Мать', '222 Мамина улица', \
                                52, '555-555-1234')
    sister_info = information.Information('Джейн Доу', '333 Ее улица', \
                                   20, '555-555-4444')
    print('Информация обо мне: ')
    display_info(my_info)
    print()
    print('Информация о матери: ')
    display_info(mom_info)
    print()
    print('Информация о сестре: ', )
    display_info(sister_info)

def display_info(information):
    print('Имя: ', information.get_name())
    print('Адрес: ', information.get_address())
    print('Возраст: ', information.get_age())
    print('Номер телефона: ' , information.get_phone())


main()