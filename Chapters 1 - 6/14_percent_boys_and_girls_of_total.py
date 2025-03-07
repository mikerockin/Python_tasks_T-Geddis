male = int(input('Введите количество мальчиков: '))
female = int(input('Введите количество девочек: '))
total = male + female
per_male = format(male / total * 100, '.2f')
per_female = format(female / total * 100, '.2f')
print(total)
print('Процент юношей равен: ', per_male, '%')
print('Процент девушек равен: ', per_female, '%')
