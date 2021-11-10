# -*- coding: utf8 -*-
import car

def main():
    # Создать экземпляр класса Car.
    my_car = car.Car('2008', 'Honda Accord')

    # Ускориться 5 раз.
    print('Автомобиль ускоряется: ')
    for i in range(5):
        my_car.accelerate()
        print('Текущая скорость: ', my_car.get_speed())
    print()

    # Притормозить 5 раз.
    print('Автомобиль замедляется: ')
    for i in range(5):
        my_car.brake()
        print('Текущая скорость: ', my_car.get_speed())


# Вызвать главную функцию.
main()






