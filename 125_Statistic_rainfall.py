def main():
    amount_months = 12
    total = 0
    average = 0
    highest = 0
    lowest = 0
    month_lowest = ''
    month_highest = ''
    rainfall_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    month_list = ['январь', 'февраль', 'март',
                  'апрель', 'май', 'июнь', 'июль',
                  'август', 'сентябрь', 'октябрь',
                  'ноябрь', 'декабрь']
    for i in range (amount_months):
        rainfall_list[i] = float(input('Введите дождевые осадки за '\
                                     + month_list[i] + ": "))
    total = sum(rainfall_list)
    average = total / amount_months
    highest = max(rainfall_list)
    month_highest = rainfall_list.index(highest)
    lowest = min(rainfall_list)
    month_lowest = rainfall_list.index(lowest)
    print('Суммарная величина  осадков:',
          format(total, '.2f'))
    print('Средняя величина дождевых осадков:',
          format(average, '.2f'))
    print('Максимальная величина дождевых осадков:',
          month_list[month_highest])
    print('Минимальная величина дождевых осадков:',
          month_list[month_lowest])


main()