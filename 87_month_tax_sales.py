def main ():
    month_volume_sales = int(input('Введите общий объем продаж за месяц: '))
    fed_tax = month_volume_sales * 0.05 / 12
    muni_tax = month_volume_sales * 0.025 / 12
    total_tax = fed_tax + muni_tax
    print('Сумма муниципального налога с продаж составляет: ', (format(muni_tax, ',.2f')))
    print('Сумма федерального налога с продаж составляет: ', (format(fed_tax, ',.2f')))
    print('Общий  налог с продаж составляет: ', total_tax)
main()
