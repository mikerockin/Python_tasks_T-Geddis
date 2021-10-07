def main():

    team = ''
    win_count = 0

    try:

        input_file = open('WorldSeriesWinners.txt', 'r')
        winners = input_file.readlines()
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip('\n')
        team = input('Введиет название команды: ')
        if team not in winners:
            print('Команда', team,
                  'никогда не выигрывала Мировую Серию.')
        else:
            for item in winners:
                if item == team:
                    win_count += 1
            print('Команда', team, 'выигрывала Мировую Серию', \
                  win_count, 'раз между 1903 и 2009 годами.')

    except IOError:
        print('Файл не найден')
    except IndexError:
        print('Ошибка индексации')
    except:
        print('Произошла ошибка')

main()
