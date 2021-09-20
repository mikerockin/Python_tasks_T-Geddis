def main():
    good_cost = int(input('Ведите сумму покупки: '))
    box = all_tax(good_cost)
    total_price = good_cost + box
    print('Сумма покупки: ', good_cost)
    print('Общий налог с продаж: ', box)
    print('Итоговая сумма: ', total_price)
def all_tax(good_cost):
    per_regional_tax = 0.025
    per_fed_tax = 0.05
    regional_tax = good_cost * per_regional_tax
    fed_tax = good_cost * per_fed_tax
    all_tax = fed_tax + regional_tax
    return all_tax
main()
