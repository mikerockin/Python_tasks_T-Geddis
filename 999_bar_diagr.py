import matplotlib.pyplot as plt

def main():
    #Создать список с координатами Х левого края каждого столбика
    left_edges = [0, 10, 20, 30, 40]
    # Создать список с высотами каждого столбика
    heights = [100, 200, 300, 400, 500]
    #Создать переменную для ширины столбика
    bar_width = 5
    #Построить столбчатую диаграмму
    plt.bar(left_edges, heights, bar_width, color =('r','g','b','m','k'))
    #Добавить заголовок
    plt.title(' Продажи с разбивкой по годам')
    # Добавить на оси описательные метки
    plt.xlabel('Год')
    plt.ylabel('Объем продаж')
    # Настроить метки делений
    plt.xticks([5, 15, 25, 35, 45], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    plt.show()
main()