# Упражнение по программированию 9-8

# Имена и адреса электронной почты

import pickle

# Глобальные константы для элементов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа с именем файла
# Файл находится в подпапке data
FILENAME = r'data\emails.dat'


# Главная функция
def main():
    # Получить словарь email.
    emails = load_emails()

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    # Обрабатывать запросы пользователя до тех пор,
    # пока пользователь не завершит работу.
    while choice != QUIT:

        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)

    # Законсервировать результирующий словарь.
    save_emails(emails)

    print('Информация сохранена.')


def load_emails():
    try:
        # Открыть файл.
        input_file = open(FILENAME, 'rb')

        # Расконсервировать словарь.
        email_dict = pickle.load(input_file)

        # Закрыть словарь.
        input_file.close()

    # Не получилось открыть словарь.
    except IOError:
        # Создать пустой словарь.
        email_dict = {}

    # Вернуть словарь.
    return email_dict


def get_user_choice():
    # Показать меню, получить выбор пользователя и
    # проверить его на допустимость
    print()
    print('Меню')
    print('------------------------------------------')
    print('1. Найти электронный адрес')
    print('2. Добавить новое имя и электронный адрес')
    print('3. Изменить существующий электронный адрес')
    print('4. Удалить имя и электронный адрес')
    print('5. Выйти из программы')
    print()

    choice = int(input('Введите свой вариант: '))

    # Проверить выбранный вариант.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введенный вами вариант неправильный. ' \
                           'Пожалуйста, введите правильный вариант: '))

    # Вернуть выбранный пользователем вариант.
    return choice


def look_up(emails):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Нацти имя в словаре.
    if name in emails:
        print('Имя:', name)
        print('Электронная почта:', emails[name])
    else:
        print('Указанное имя не найдено.')


def add(emails):
    # Получить имя и электронный адрес.
    name = input('Введите имя: ')
    address = input('Введите электронный адрес: ')

    # Добавить новый адрес, если имя не существует.
    # В противном случае уведомить пользователя, что имя существует.
    if name not in emails:
        emails[name] = address
        print('Имя и электронный адрес были добавлены.')
    else:
        print('Это имя уже существует.')


def change(emails):
    # Получить имя для обновления информации.
    name = input('Введите имя: ')

    # Изменить адрес, если имя существует.
    # В противном случае уведомить пользователя, что не имя существует.
    if name in emails:
        address = input('Введите новый адрес: ')
        emails[name] = address
        print('Информация обновлена.')
    else:  # name not found
        print('Указанное имя не найдено.')


def delete(emails):
    # Получить имя для удаления.
    name = input('Введите имя: ')

    if name in emails:

        del emails[name]
        print('Информация удалена.')

    else:  # имя не найдено
        print('Указанное имя не найдено.')


# Функция консервирует указанный словарь и
# сохраняет его в файле emails.
def save_emails(emails):
    # Открыть файл для записи.
    output_file = open(FILENAME, 'wb')

    # Законсервировать словарь и его сохранить.
    pickle.dump(emails, output_file)

    # Закрыть файл.
    output_file.close()


# Вызвать главную функцию.
main()
