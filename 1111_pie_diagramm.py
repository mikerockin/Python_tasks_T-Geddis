import matplotlib.pyplot as plt
def main():
    # Создать список объемов продаж
    sales = [100,400,300,600]
    # Создать список меток долей
    slice_labels = ['1-й кв', '2-й кв','3-й кв', '4-й кв']
    # Создать из этих значений круговую диаграмму
    plt.pie(sales, labels=slice_labels, colors=('r','g','b','k'))
    # Добавить заголовок
    plt.title('Продажи с разбивкой по кварталам')
    plt.show()
main()