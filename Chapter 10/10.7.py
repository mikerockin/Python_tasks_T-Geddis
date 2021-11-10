# -*- coding: utf8 -*-
import emp
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employess.dat'

def main():
    employees = load_employees()
    choice = 0

    while choice != QUIT:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

    save_employees(employees)

def load_employees():
    try:
        input_file = open(FILENAME, 'rb')

        employee_dict = pickle.load(input_file)

        input_file.close()
    except IOError:
        employee_dict = {}

    return employee_dict

def get_user_choice():

    print()
    print('Меню')
    print('-------------------------------------')
    print('1. Найти сотрудника')
    print('2. Добавить нового сотрудника')
    print('3. Изменить существующего сотрудника')
    print('4. Удалить сотрудника')
    print('5. Выйти из программы')
    print()

    choice = int(input('Введите свой выбор: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введенный вами выбор недопустимый'))
    return choice

def look_up(employees):
    name = input('Введите имя сотрудника: ')
    ID = input('Введите идентификатор сотрудника: ')
    department = input('Введите отдел сотрудника: ')
    title = input('Введите должность сотрудника: ')

    new_emp = emp.Employee(name, ID, department,title)

    if ID not in employees:
        employees[ID] = new_emp
        print('Новый сотрудник был добавлен')
    else:
        print('Сотрудник с этим идентификатором уже существует')

def change(employees):
    ID = input('Введите идентификатор сотрудника')
    if ID in employees:
        name = input('Введите новое имя: ')
        department = input('Введите новый отдел: ')
        title = input('Введите новую должность: ')

        new_emp = emp.Employee(name,ID, department,title)

        employees[ID] = new_emp
        print('Информация о сотруднике обновлена')

    else:
        print('Указанный идентификатор не найден')

def delete(employees):
    ID = input('Введите идентификатор сотрудника: ')
    if ID in employees:
        del employees[ID]
        print('Информация о сотруднике удалена')
    else:
        print('Указанный идентификатор не найден')

def save_employees(employees):
    output_file = open(FILENAME, 'wb')
    pickle.dump(employees, outputfile)
    output_file.close()

main()





