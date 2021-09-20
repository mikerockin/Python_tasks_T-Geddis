def main():
    print('Данная программа показывает оценочную стоимость недвижимости: ')
    print('А также налог на имущество: ')
    cost_build = int(input('Введите фактическую стоимость недвижимости: '))
    est_cost = estimated_cost(cost_build)
    box = tax_immovable(est_cost)
    print('Стоимость недвижимости', cost_build)
    print('Оценочная стоимость составит: ', est_cost )
    print('Налог на имуществово составит:', format(box, ',.2f'))
def estimated_cost(cost):
    est_cost = cost * 0.6
    return est_cost
def tax_immovable(cost):
    tax = cost / 100 * 0.72
    return tax
main()
