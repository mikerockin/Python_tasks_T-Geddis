# -*- coding: utf8 -*-
import pet

def main():
    pet_name = ''
    pet_type = ''
    pet_age = 0

    pet_name = input('Введите имя домашнего питомца: ')
    pet_type = input('Введите вид животного: ')
    pet_age = int(input('Введите возраст животного: '))

    my_pet = pet.Pet(pet_name, pet_type, pet_age)

    print('Вот такие данные вы ввели')
    print('Имя домашнего питомца: ', pet_name)
    print('Вид животного: ', pet_type)
    print('Возраст животного: ', pet_age)

main()




