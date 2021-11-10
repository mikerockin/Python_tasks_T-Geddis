# -*- coding: utf8 -*-
import patient
import procedure

def main():

    procedure_1 = procedure.Procedure('Врачебный осмотр' , 'Сегодняшняя', ' Ирвин', 250.00)
    procedure_2 = procedure.Procedure('Рентгеноскопия', 'Сегодняшняя', ' Джемисон', 500.00)
    procedure_3 = procedure.Procedure('Анализ крови', 'Сегодняшняя', ' Смит', 200.00)

    pat = patient.Patient('Иван', 'Петрович' , 'Кукрыниксенко', 'Садовое кольцо 19', 'Сыктывкар', 'Пермский край', '457383', '9898', 'Евлампий', '987455')

    print(pat)
    print('Процедура № 1')
    print(procedure_1)
    print('Процедура № 2')
    print(procedure_2)
    print('Процедура № 3')
    print(procedure_3)

main()