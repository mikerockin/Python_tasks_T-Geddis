def main():
    cost_build = int(input('Введите стоимость строения для расчета суммы страховки: '))
    cost_of_insurance = insurance(cost_build)
    print('Стоимость строения: ', cost_build)
    print('Минимальная сумма страховки составит: ', cost_of_insurance)
def insurance(cost):
    cost_of_insurance = cost * 0.8
    return cost_of_insurance
main()
