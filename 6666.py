# Упражнение по программированию 7-15

# График еженедельных цен на бензин за 1994 год

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (7, 6)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# Именованная константа
NUM_WEEKS = 52

def main():
    # Открыть файл цен на бензин.
    # Файл находится в подпапке data
    gas_file = open('1994_Weekly_Gas_Averages.txt', 'r')

    # Прочитать содержимое файла в список.
    gas = gas_file.readlines()

    # Закрыть файл.
    gas_file.close()

    # Отсечь символ новой строки из каждого элемента.
    for i in range(len(gas)):
        gas[i] = gas[i].rstrip('\n')

    # Создать список с номерами недель
	# (чтобы использовать в качестве координат x).
    x_coords = []
    for i in range(1, NUM_WEEKS + 1):
        x_coords.append(i)

    # Построить линейный график.
    plt.plot(x_coords, gas)

    # Ограничить ось X диапазоном между 1-52.
    plt.xlim(xmin=1, xmax=NUM_WEEKS)

    # Добавить заголовок.
    plt.title('Средненедельные цены на бензин в 1994 г.')

    # Добавить метки к осям.
    plt.xlabel('Недели (по номеру)')
    plt.ylabel('Средние цены')

    # Показать график.
    plt.show()

# Вызвать главную функцию
main()