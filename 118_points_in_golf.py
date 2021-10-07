def main():
    func_write = write()
    func_read = read()
def write():
    player_num = int(input('Введите количество игроков по которым вы хотите внести информацию: '))
    outfile = open('points_in_golf.txt', 'w')
    for count in range (1, player_num + 1):
        print('Введите данные об игроках:')
        name = input('Имя: ')
        points = input('Количество очков: ')
        outfile.write(name + '\n')
        outfile.write(points + '\n')
        print()
    outfile.close()
    print('Записи об игроках сохранены в points_in_golf.txt ')
def read():
    print('Данные считаны из ранее записанного файла:')
    infile = open('points_in_golf.txt', 'r')
    name = infile.readline()
    while name != '':
        points = infile.readline()
        name = name.rstrip('\n')
        points = points.rstrip('\n')
        print('Name: ' , name)
        print('Points: ', points)
        name = infile.readline()
    infile.close()
main()

while line != '':
    answer += 1
    line = line.rstrip('\n')
    print('Answer №', answer, line)
    line = infile.readline()
infile.close()

ef read_readlines():
    answer = 0
    print('Данные полученных ответов считаны:')
    infile = open('user_answers.txt', 'r')
    line = infile.readlines()
    while line != '':
        answer += 1
        line = line.rstrip('\n')
        print('Answer №', answer, line)
        line = infile.readline()
    infile.close()