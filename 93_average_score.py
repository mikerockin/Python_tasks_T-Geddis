def main():
    print('Сейчас вам предстоит ввести 5 экзаменационных оценок')
    grade_1 = int(input('Введите оценку: '))
    grade_2 = int(input('Введите оценку: '))
    grade_3 = int(input('Введите оценку: '))
    grade_4 = int(input('Введите оценку: '))
    grade_5 = int(input('Введите оценку: '))
    determine_1 = determine_grade(grade_1)
    determine_2 = determine_grade(grade_2)
    determine_3 = determine_grade(grade_3)
    determine_4 = determine_grade(grade_4)
    determine_5 = determine_grade(grade_5)
    print('Оценки по шкале классификации в введенной последовательности: ')
    print('По шкале классификации: ', determine_1)
    print('По шкале классификации: ', determine_2)
    print('По шкале классификации: ', determine_3)
    print('По шкале классификации: ', determine_4)
    print('По шкале классификации: ', determine_5)
    average = calc_average(grade_1,grade_2,grade_3,grade_4,grade_5)
    print('Средний балл: ', average)
def determine_grade(grade):
    if grade >= 90:
        grade = 'A'
    elif grade >= 80 and  grade <= 89:
        grade = 'B'
    elif grade >= 70 and grade <= 79:
        grade = 'C'
    elif grade >= 60 and grade <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade
def calc_average(a,b,c,d,e):
    average = a + b + c + d +e
    return average
main()
