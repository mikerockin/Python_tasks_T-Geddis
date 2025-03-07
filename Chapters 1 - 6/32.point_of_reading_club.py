amount_books = int(input('Введите количество книг преобретенных в этом месяце'))
if amount_books ==0:
    print('Вы не купили ни одной книги в этом месяце, у вас 0 очков')
elif amount_books == 2:
    print('Количество ваших очков: 5 ')
elif amount_books == 4:
    print('Количество ваших очков: 15 ')
elif amount_books == 6:
    print('Количество ваших очков: 30 ')
elif amount_books >= 8:
    print('Количество ваших очков: 60 ')
