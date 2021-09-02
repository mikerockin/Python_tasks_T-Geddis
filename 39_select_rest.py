print('Необходимо ответить на несколько вопросов по пикнику: ')
vegtr_list = 'Центральная пиццерия','Кофе за углом','Блюда от Итальянской мамы','Кухня шеф-повара'
vegan_list = 'Кофе за углом','Кухня шеф-повара'
glutens_list = 'Центральная пиццерия','Кофе за углом','Кухня шеф-повара'
vegtr_vegan_list = vegan_list
vegan_gluten = vegan_list
vegtr_gluten = glutens_list
vegtr_vegan_gluten = vegan_list
nobody = 'Центральная пиццерия','Кофе за углом','Блюда от Итальянской мамы','Кухня шеф-повара', 'Изысканные гамбергеры от Джо'
ans_1 = str(input('Будет ли на ужине вегетарианец?'))
ans_2 = str(input('Будет ли на ужине веганец?'))
ans_3 = str(input('Будет ли на ужине приверженец безглютеновой диеты?'))
if ans_1 == 'yes' and ans_2 == 'no' and ans_3 == 'no':
    print('Подходящие рестораны:')
    print(vegtr_list)
elif ans_1 == 'no' and ans_2 == 'yes' and ans_3 == 'no':
    print('Подходящие рестораны:')
    print(vegan_list)
elif ans_1 == 'no' and ans_2 == 'no' and ans_3 == 'yes':
    print('Подходящие рестораны:')
    print(glutens_list)
elif ans_1 == 'yes' and ans_2 == 'yes' and ans_3 == 'no':
    print('Подходящие рестораны:')
    print(vegtr_vegan_list)
elif ans_1 == 'yes' and ans_2 == 'no' and ans_3 == 'yes':
    print('Подходящие рестораны:')
    print(vegtr_gluten)
elif ans_1 == 'no' and ans_2 == 'yes' and ans_3 == 'yes':
    print('Подходящие рестораны:')
    print(vegan_gluten)
elif ans_1 == 'yes' and ans_2 == 'yes' and ans_3 == 'yes':
    print('Подходящие рестораны:')
    print(vegtr_vegan_gluten)
elif ans_1 == 'no' and ans_2 == 'no' and ans_3 == 'no':
    print('Подходящие рестораны:')
    print(nobody)


