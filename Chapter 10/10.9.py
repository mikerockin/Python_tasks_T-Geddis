# -*- coding: utf8 -*-
import question

def main():

    first_points = 0
    second_points = 0
    player = ''

    questions = get_questions()

    for i in range (10):

        if i % 2 ==0:
            player = 'Один'
        else:
            player = 'Два'
        print('Вопрос для игрока ', player, ':')

        current = questions[i]
        print(current)
        user_answer = int(input('Введите ваше решение (номер' + \
                                            ' между 1 и 4): '))
        if current.isCorrect(user_answer):
            if player == 'Один':
                first_points += 1
            else:
                second_points += 1
            print('Это правильный ответ.')
            print()
        else:
            print('Неправильно. Правильный отет', \
                  current.get_solution())
            print()
        print('Первый игрок заработал', first_points, 'очков.')
        print('Второй игрок заработал', second_points, 'очков.')
        if first_points == second_points:
            print('Ничья.')
        elif first_points > second_points:
            print('Первый игрок побеждает в игре.')
        else:
            print('Второй игрок побеждает в игре.')

def get_questions():
    questions = []

    question1 = question.Question('Сколько дней в лунном ' + \
                                  'году?', '354', '365', \
                                  '243', '379', 1)
    questions.append(question1)
    question2 = question.Question('Какая самая большая планета?', \
                                  'Марс', 'Юпитер', 'Земля', \
                                  'Плутон', 2)
    questions.append(question2)
    question3 = question.Question('Какой кит самый ' + \
                                  'большой?', 'Косатка', \
                                  'Горбатый кит', \
                                  'Белуга', 'Синий кит', 4)
    questions.append(question3)
    question4 = question.Question('Какой динозавр мог летать?', \
                                  'Трицератопс', 'Тираннозавр', \
                                  'Птеранодон', 'Диплодок', 3)
    questions.append(question4)
    question5 = question.Question('Какой из этих героев книги ' + \
                                  'о Винни Пухе является осликом?', \
                                  'Пух', 'Иа-Иа', 'Пятачок', \
                                  'Канга', 2)
    questions.append(question5)
    question6 = question.Question('Какая из них самая жаркая планета?', \
                                  'Марс', 'Плутон', 'Земля', \
                                  'Венера', 4)
    questions.append(question6)
    question7 = question.Question('У какого динозавра был самый ' + \
                                  'большой мозг по сравнению с ' + \
                                  ' телом тела?', 'Троодон', \
                                  'Стегозавр', \
                                  'Ихтиозавр', 'Гигантораптор', 1)
    questions.append(question7)
    question8 = question.Question('Какой из пингвинов самый ' + \
                                  'крупный?', \
                                  'Антарктический пингвин', \
                                  'Золотоволосый пингвин', \
                                  'Императорский пингвин', \
                                  'Белокрылый пингвин', 3)
    questions.append(question8)
    question9 = question.Question("В какой сказке героем " + \
                                  'является обезъянка?', \
                                  'Винни Пух', \
                                  'Любопытный Джордж', 'Хортон', \
                                  'Гуфи', 2)
    questions.append(question9)
    question10 = question.Question('Сколько длится год на Марсе?', \
                                   '550 земных дней', \
                                   '498 земных дней', \
                                   '126 земных дней', \
                                   '687 земных дней', 4)
    questions.append(question10)

    return questions

main()
