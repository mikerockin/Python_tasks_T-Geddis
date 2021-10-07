def main():
    # Определить переменные
    yearly_change = []
    change = 0.0
    total_change = 0.0
    average_change = 0.0
    greatest_increase = 0.0
    smallest_increase = 0.0
    greatest_year = 0
    smallest_year = 0

    # Константа для базового года
    BASE_YEAR = 1950

    try:
        # Открыть файл для чтения.
        # Файл находится в подпапке data
        input_file = open('USPopulation.txt', 'r')

        # Прочитать все строки из файла в список.
        yearly_population = input_file.readlines()

        # Преобразовать все строковые значения в числа.
        for i in range(len(yearly_population)):
            yearly_population[i] = float(yearly_population[i])

        # Вычислить изменение в численности населения
        # по каждым двум годам.
        for i in range(1, len(yearly_population)):
            change = yearly_population[i] - yearly_population[i - 1]
            yearly_change.append(change)

            # Если это первый год, то присвоить отслеживающим
            # переменным значение этого года.
            if i == 1:
                greatest_increase = change
                smallest_increase = change
                greatest_year = 1
                smallest_year = 1

            # Это не первое изменение в численности населения.
            # При необходимости обновить отслеживающие переменные.
            else:
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_year = i

                elif change < smallest_increase:
                    smallest_increase = change
                    smallest_year = i

        total_change = float(sum(yearly_change))
        average_change = total_change / len(yearly_change)

        print('Среднегодовое изменение в численности ' \
              'во время этого периода времени составило',
              format(average_change, ',.2f'))
        print('Год с максимальным ростом численности', \
              BASE_YEAR + greatest_year)
        print('Год с минимальным ростом численности', \
              BASE_YEAR + smallest_year)

    # Обработать любые ошибки, которые могут произойти.
    except IOError:
        print('Файл не найден')
    except IndexError:
        print('Ошибка индексации')
    except:
        print('Произошла ошибка')


# Вызвать главную функцию.
main()

