MONTHS_IN_A_YEAR = 3
def main():
    name_of_months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                  'Ноябрь', 'Декабрь']
    rainfall_list = get_rainfall_amounts(name_of_months)
    total_rainfall = int(calculate_total_rainfall(rainfall_list))
    average_rainfall = calculate_average_rainfall(total_rainfall, len(rainfall_list))
    min_amount_rainfall = calculate_min_amount_raunfall(rainfall_list, name_of_months)
    max_amount_rainfall = calculate_min_amount_raunfall(rainfall_list, name_of_months)
    print_Rainfall_statistic(rainfall_list, name_of_months, total_rainfall, average_rainfall, min_amount_rainfall,
                             max_amount_rainfall)
    print('Список с количеством осадков' , rainfall_list)
    print('Общее количество осадков зв год : ', total_rainfall)
    print('Среднемесячное количество осадков: ', format(average_rainfall, ',.2f'))
    print('Минимальное количество осадков: ', min_amount_rainfall)
    print('Максимальное количество осадков: ', min_amount_rainfall)
def get_rainfall_amounts (name_of_months):
    rainfall_years = []
    for r in range (MONTHS_IN_A_YEAR):
        user_rainfall = input('Введите количество осадков: ')
        rainfall_years.append(user_rainfall)
    return rainfall_years
def calculate_total_rainfall(rainfall_years):
    total_rainfall = 0
    for values in rainfall_years:
        total_rainfall += values
    return total_rainfall
def calculate_average_rainfall(total_rainfall, rainfall_list):
        average_months = total_rainfall / rainfall_list
        return average_months
def calculate_min_amount_raunfall(rainfall_list, name_of_months):
    min_ra = min(rainfall_list)
    index = rainfall_list.index(min_ra)
    print(min_ra)
    print(index)
    return name_of_months[index]
def calculate_min_amount_raunfall(rainfall_list, name_of_months):
    max_ra = max(rainfall_list)
    index = rainfall_list.index(max_ra)
    print(max_ra)
    print(index)
    return name_of_months[index]
def print_Rainfall_statistic (rainfall_list, name_of_months, total_rainfall,  average_rainfall, min_amount_rainfall, max_amount_rainfall):
    for current_month_index in range (len(name_of_months)):
        print(name_of_months [current_month_index], 'Получено количество осадков в', rainfall_list[current_month_index])
main()