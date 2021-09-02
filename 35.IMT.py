weight = float(input('Введите свой вес'))
height = float(input('Введите свой рост'))
imt = weight / ((height / 100) ** 2)
if imt >= 18.5 and imt <= 25:
    print(imt, 'Оптимальная масса тела!')
elif imt < 18.5:
    print(imt, 'Масса ниже нормы!')
elif imt > 25:
    print(imt, 'Масса выше нормы!')
