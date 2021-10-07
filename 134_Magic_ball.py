import random
def main():
    infile = open('8_ball_responses.txt', 'r')
    choices = infile.readlines()
    for i in range(len(choices)):
        choices[i] = choices[i].rstrip('\n')
    answer = random.choice(choices)
    question = input('Введите вопрос, подразумевающий ответ "Да" или "Нет": ')
    print('Ответ на ваш вопрос: ', question)
    print(answer)

main()