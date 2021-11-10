# -*- coding: utf8 -*-

import person

def main():

    name = ''
    address = ''
    phone_number = ''
    client_number = 0
    on_list_flag = False

    name = input('Введите имя: ')
    address = input('Введите адрес: ')
    phone_number = input('Введите номер телефона: ')
    client_number = input('Введите номер клиента: ')
    on_list = input('Хочет ли клиент быть в списке ' \
                    'рассылки? (Да/Нет) ')
    if on_list == 'Да':
        on_list_flag = True
    else:
        on_list_flag = False

    customer = person.Customer(name, address, phone_number,client_number, on_list_flag)

    print('Информация о клиенте: ')
    print('Имя: ', customer.get_name())
    print('Адресс: ', customer.get_address())
    print('Номер телефона контакта: ', customer.get_phone_n())
    print('Номер клиента: ', customer.get_client_number())
    print('В списке рассылки: ', customer.get_spam())

main()

