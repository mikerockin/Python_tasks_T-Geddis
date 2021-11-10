# -*- coding: utf8 -*-
import employee

def main():

    super_name = ''
    super_id = ''
    super_salary = 0.0
    super_bonus = 0.0

    super_name = input('Введите имя начальника смены: ')
    super_id = input('Введите id номер: ')
    super_salary = float(input('Введите данные по годовому окладу: '))
    super_bonus = float(input('Введите размер годовой премии: '))

    supervisor = employee.ShiftSupervisor(super_name, super_id, super_salary, super_bonus)

    print('Информация о начальнике смены: ')
    print('Имя: ', supervisor.get_name())
    print('Номер id:', supervisor.get_id_number())
    print('Годовой оклад:', supervisor.get_year_pay())
    print('Годовая премия:', supervisor.get_year_prize())

main()



