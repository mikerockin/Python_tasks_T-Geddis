def main():
    print('Эта программа расчитывает ваши расходы на автомобиль')
    print('Сейчас вам потребуется ввести месячные расходы на каждый пункт в рублях')
    credit_paid = int(input('Введите платеж по кредиту: '))
    insurance = int(input('Введите стоимость страховки: '))
    gasoline = int(input('Введите затраты на бензин: '))
    oil = int(input('Введите затраты на масло: '))
    tires = int(input('Введите затраты на шины: '))
    to = int(input('Введите затраты на техническое обслуживание: '))
    months_expenses = credit_paid + insurance + gasoline + oil + tires + to
    year_expenses = months_expenses * 12
    print('Месячные расходы составят: ', months_expenses)
    print('Годовые расходы составят: ', year_expenses)
main()

