# Упражнение по программированию 8-13_1_2

# Лотерея PowerBall - распространенность чисел

# Именованная константа
LOTTERY_NUMBERS = 69


# Функция get_all_numbers возвращает список с лотерейными
# числами файла pbnumbers.txt. Числа появляются в том
# порядке, в каком они были прочитаны из файла.
def get_all_numbers():
    # Открыть файл с лотерейными числами.
    # Файл находится в подпапке data
    pblottery_file = open(r'data\pbnumbers.txt', 'r')

    # Прочтитать содержимое файла в список.
    pblottery = pblottery_file.readlines()

    # Закрыть файл.
    pblottery_file.close()

    # Удалить из каждого элемента символ новой строки.
    for i in range(len(pblottery)):
        pblottery[i] = pblottery[i].rstrip('\n')

    # Разбить каждый элемент на отдельные числа и сохранить
    # отдельные регулярные числа в списке под названием lotto_nums.
    lotto_nums = []
    for i in range(len(pblottery)):
        number_set = pblottery[i].split()
        for j in range(len(number_set)):
            lotto_nums.append(int(number_set[j]))

    # Вернуть список lotto_nums.
    return lotto_nums


# Функция get_frequency принимает список чисел и определяет
# частоту каждого значения в списке. Параметр max_value
# обозначает максимальное значение, хранящееся в списке.
def get_frequency(number_list, max_value):
    # Создать список для частоты каждого числа.
    # Каждый элемент списка инициализируется нулем.
    frequency = [0] * (max_value + 1)
    for i in range(len(number_list)):
        # Получить следующее лотерейное число в списке.
        num = number_list[i]

        # Увеличить частоту этого числа.
        frequency[num] += 1

    # Вернуть частотный список.
    return frequency


# Функция position_of_highest_value возвращает позицию
# самого большого значения в списке num_list.
def position_of_highest_value(num_list):
    highest = 0
    highest_position = 0
    for i in range(len(num_list)):
        if num_list[i] > highest:
            highest = num_list[i]
            highest_position = i

    return highest_position


# Функция most_common принимает частотный список freq_list и возвращает
# другой список, в котором элемент 0 содержит позицию самого большого
# значения в списке freq_list, элемент 1 содержит позицию второго
# самого большого значения в списке freq_list, и т.д.
def most_common(freq_list):
    # Создать пустой список для позиций самых распространенных значений.
    common_sorted = []

    # Сделать копию списка freq_list.
    temp_list = []
    for item in freq_list:
        temp_list.append(item)

    for i in range(len(temp_list)):
        position = position_of_highest_value(temp_list)
        common_sorted.append(position)
        temp_list[position] = -1

    # Вернуть список common_sorted.
    return common_sorted


def main():
    # Получить список всех лотерейных чисел.
    lotto_nums = get_all_numbers()

    # Получить частоту каждого числа.
    frequency = get_frequency(lotto_nums, LOTTERY_NUMBERS)

    # Получить список наиболее распространенных значений.
    sorted_by_most_common = most_common(frequency)

    # Показать 10 наиболее распространенных чисел.
    print('10 наиболее распространенных чисел (по убыванию)')
    print('------------------------------------------------')
    for i in range(10):
        print(sorted_by_most_common[i])

    # Показать 10 наименее распространенных чисел.
    sorted_by_most_common.reverse()
    print('\n10 наиболее распространенных чисел (по возрастанию)')
    print('---------------------------------------------------')
    for i in range(1, 11):
        print(sorted_by_most_common[i])


# Вызвать главную функцию
main()
