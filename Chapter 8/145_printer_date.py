
def main():
    day = 0
    month_num = 0
    month_name = ''
    date_string = ''
    months_list = ['январь', 'февраль', 'март',
                  'апрель', 'май', 'июнь', 'июль',
                  'август', 'сентябрь', 'октябрь',
                  'ноябрь', 'декабрь']
    date_string = input('Введите дату в формате дд/мм/гггг: ')
    date_list = date_string.split('/')
    day = date_list[0]
    month_num = int(date_list[1])
    print(month_num)
    year = date_list[2]
    month_name = months_list[month_num - 1]
    long_date = day + ' ' + month_name + ' '+  year
    print(long_date)
main()
