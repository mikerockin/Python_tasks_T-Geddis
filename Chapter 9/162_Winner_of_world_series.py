BASE_YEAR= 1903
def main():
    year_dict = {}
    count_dict = {}
    infile = open('WorldSeriesWinners.txt', 'r')
    winners = infile.readlines()
    for i in range(len(winners)):
        team = winners[i].rstrip('\n')
        year = BASE_YEAR + i
        if year >= 1904:
            year += 1
        if year >= 1994:
            year += 1
        year_dict[str(year)] = team
    if team in count_dict:
        count_dict[team] += 1
    else:
        count_dict[team] = 1
    year = input('Введите год от 1903 до 2009: ')

    if year == '1904' or year == '1994':
        print('Мировая серия не проводилась в ', year)
    elif year < '1903' or year > '2009':
        print('Даные за: ', year, 'не включены в базу данных')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
    print('Командой, которая стала победителем Мировой Серии в ', \
          year, ' году, была ', winner, '.', sep='')
    print('Они побеждали в Мировой Серии', wins, 'раз.')
main()