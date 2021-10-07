def main():
    solution = ['A', 'C', 'A', 'A', 'D',
                'B', 'C', 'A', 'C', 'B',
                'A', 'D', 'C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']
    correct_count = 0
    incorrect_count = 0
    incorrect_answers = []
    counter = 0
    try:
        input_file = open('student_solution.txt', 'r')
        student_solutions = input_file.readlines()
        for i in range(len(student_solutions)):
            student_solutions[i] = student_solutions[i].rstrip('\n')
        for i in range(len(student_solutions)):
            if student_solutions[i] == solution[i]:
                correct_count += 1
            else:
               incorrect_count += 1
               incorrect_answers.append(str(i + 1))
        if correct_count >= 15:
            print('Поздравляем, вы прошли экзамен')
        else:
            print('Вы не сдали экзамен')
        print('Количество вопросов на которые вы ответили верно' , correct_count)
        print('Колчичество вопросов на которые вы ответили неверно', incorrect_count)
        if incorrect_count >0:
            print('Вопросы на которые вы ответили неправильно: ')
            while counter < incorrect_count:
                print(incorrect_answers[counter], end='')
                if counter + 1 < incorrect_count:
                    print(', ', end='')
                counter += 1
    except IOError:
        print('Файл не найден')
    except IndexError:
        print('Ошибка индексации')
    except:
        print('Произошла ошибка')

main()