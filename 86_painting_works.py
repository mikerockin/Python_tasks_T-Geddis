def main():
    walls_area = int(input('Введите площадь поверхности окрашиваемой стены: ')) / 10
    cost_paint = int(input('Введите стоимость 5- литровой банки с краской: '))
    jars_of_paint = walls_area * 5
    times = walls_area * 8
    print('Количество требующихся емкостей краски: ', jars_of_paint,)
    print('Количество требующихся часов: ', times)
    print('Стоимость краски: ', jars_of_paint * cost_paint)
    print('Стоимость работы: ', times * 2000)
    print('Общая стоимость: ', (jars_of_paint * cost_paint) + (times * 2000))
main()
