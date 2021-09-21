def main():
    sum = int(input('Введите текущую сумму на счете: '))
    per_bet = float(input('Введите ежемесячную процентную ставку: ')) / 100
    monts_sum = int(input('Введите количество месяцев, которое деньги будут находится на счете: '))
    total = future_cost(sum, per_bet,monts_sum)
    print('Будущая сума на счете составит: ', format(total, ',.2f'))
def future_cost(sum, perbet,monts):
    fut_cost = sum * ((perbet + monts)**2)
    return fut_cost
main()

