def main():
    fats = int(input('Введите потребляемое количество жиров в граммах: '))
    carbohydrate = int(input('Введите потребляемое количество углеводов в граммах: '))
    fat = amount_fats(fats)
    carbonhydrt = amount_carbohydrate(carbohydrate)
    print('Количество калорий в результе употребления жиров составило: ', fat)
    print('Количество калорий в результе употребления углеводов составило: ', carbonhydrt)
def amount_fats(fats):
    kcal = fats * 9
    return kcal
def amount_carbohydrate(carbohydrate):
    kcal = carbohydrate * 4
    return kcal
main()
