names = ['Perl', 'Gorg', 'Plov', 'Ruby']
search = input('Введите имя: ') # search может быть равен Ruby изначально
if search in names:
    print('Hello, Ruby!')
else:
    print('Sorry, not found!')