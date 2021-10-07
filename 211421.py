MONTHS_IN_A_YEAR = 3
def get_rainfall_amounts (name_of_months):
    MONTHS_IN_A_YEAR = 3
    rainfall_years = []
    for current_month_index in range (MONTHS_IN_A_YEAR):
        user_rainfall = input('Введите количество осадков : ' +\
                              name_of_months[current_month_index])
        rainfall_years.append(user_rainfall)
    return rainfall_years
def calculate_total_rainfall(rainfall_years):
    total_rainfall = 0
    for values in range(len(rainfall_years)):
        total_rainfall = total_rainfall + values
    return total_rainfall
def calculate_average_rainfall(rainfall_list):
    number_of_months = len(rainfall_list)
    average_months = calculate_total_rainfall(rainfall_list) / number_of_months
    return average_months
def calculate_min_amount_raunfall(rainfall_list, name_of_months):
    min_ra = min(rainfall_list)
    index = rainfall_list.index(min_ra)
    return name_of_months[index]
def calculate_max_amount_rainfall(rainfall_list, name_of_months):
    max_ra = max(rainfall_list)
    index = rainfall_list.index(max_ra)
    return name_of_months[index]
def print_Rainfall_statistics (rainfall_list, name_of_months, total_rainfall,  average_rainfall, min_amount_rainfall, max_amount_rainfall):
    print()
    for current_month_index in range (len(name_of_months)):
        print(name_of_months [current_month_index], 'Получено количество осадков в', rainfall_list[current_month_index])
    print('Список с количеством осадков', rainfall_list)
    print('Общее количество осадков зв год : ', total_rainfall)
    print('Среднемесячное количество осадков: ', format(average_rainfall, ',.2f'))
    print('Минимальное количество осадков: ', min_amount_rainfall)
    print('Максимальное количество осадков: ', max_amount_rainfall)
def main():
    name_of_months = ['Январь ', 'Февраль ', 'Март ', 'Апрель ', 'Май ', 'Июнь ', 'Июль ', 'Август ', 'Сентябрь ', 'Октябрь ',
                  'Ноябрь ', 'Декабрь ']
    rainfall_list = []
    rainfall_list = get_rainfall_amounts(name_of_months)
    total_rainfall = calculate_total_rainfall(rainfall_list)
    average_rainfall = calculate_average_rainfall(rainfall_list)
    min_amount_rainfall = calculate_min_amount_raunfall(rainfall_list, name_of_months)
    max_amount_rainfall = calculate_max_amount_rainfall(rainfall_list, name_of_months)
    print_Rainfall_statistics(rainfall_list, name_of_months, total_rainfall, average_rainfall, min_amount_rainfall,
                             max_amount_rainfall)
main()