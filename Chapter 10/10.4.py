# -*- coding: utf8 -*-
import emp

def main():
    emp_1 = emp.Employee('Сьюзан Мейерс', '47899',
                        'Бухгалтерия', 'Вице-президент')
    emp_2 = emp.Employee('Марк Джоунс', '39119',
                        'ИТ', 'Программист')
    emp_3 = emp.Employee('Джой Роджерс', '81774',
                        'Производственный', 'Инженер')

    print('Сотрудник № 1')
    print(emp_1)
    print()
    print('Сотрудник № 2')
    print(emp_2)
    print()
    print('Сотрудник № 3')
    print(emp_3)

main()
