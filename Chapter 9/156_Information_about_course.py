def main():
    dct_course_room = {'CS101': '3004', 'CS102': '4501', 'CS103':'6755', 'CS104':'1244', 'CS105':'1411'}
    dct_course_teach = {'CS101': 'Хайнс', 'CS102': 'Альварадо', 'CS103':'Рич', 'CS104':'Берк', 'CS105':'Ли'}
    dct_course_time = {'CS101': '08:00', 'CS102': '09:00', 'CS103':'10:00', 'CS104':'11:00', 'CS105':'13:00'}
    user_choice = input('Введите номер курса: ')
    if user_choice not in dct_course_room:
        print('Такого курса не существует')
    else:
        print('Подробные данные относительно курса:', user_choice)
        print('Номер аудитории: ', dct_course_room[user_choice])
        print('Имя преподавателя: ', dct_course_teach[user_choice])
        print('Время начала занятия: ', dct_course_time[user_choice])
main()

