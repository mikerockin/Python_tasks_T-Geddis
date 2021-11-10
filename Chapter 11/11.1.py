# -*- coding: utf8 -*-
import employee

def main():

    # Создаем локальные переменные:

    worker_name = ''
    worker_id = ''
    worker_shift = 0
    worker_tax = 0.0

    worker_name = input('Введите имя сотрудника: ')
    worker_id = input ('Введите номер сотрудника: ')
    worker_shift = int(input('Введите номер смены: '))
    worker_tax = float(input('Введите часовую ставку оплаты труда: '))

    worker = employee.ProductionWorker(worker_name, worker_id, worker_shift, worker_tax)

    print('Информация о рабочем')
    print('Имя:', worker.get_name())
    print('Идентификатор:', worker.get_id_number())
    print('Смена:', worker.get_number_s())
    print('Ставка оплаты труда: ', format(worker.get_tax(), ',.2f'))

main()






