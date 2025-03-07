import contact
import pickle
LOOK_UP = 1
ADD = 2
CHNGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():
    mycontacts = load_contacts()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice ==ADD:
            add(mycontacts)
        elif choice == CHNGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    save_contacts(mycontacts)

def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contact_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        contact_dct = {}
    return contact_dct

def get_menu_choice():
    print()
    print('Меню ')
    print('--------------------------------')
    print('1. Найти контакт')
    print('2. Добавить новый контакт')
    print('3. Изменить существующий контакт')
    print('4. Удалить контакт')
    print('5. Выйти из программы')
    print()
    choice  = int(input('Введите выбранный пункт'))
    while choice <LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт'))
    return choice
def look_up(mycontacts):
    name = input('Введите имя')
    print(mycontacts.get(name, 'Это имя не найдено.'))

def add(mycontacts):
    name = input('Имя: ')
    phone = input ('Телефон: ')
    email = input ('Электронный адрес: ')
    entry = contact.Contact(name, phone, email)
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена')
    else:
        print('Это имя уже существует')

def change(mycontacts):
    name = input('Введите имя:')
    if name in mycontacts:
        phone = input('Введите новый телефонный номер')
        email = input('Введите новый электронный адрес')
        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Информация обновлена')
    else:
        print('Это имя не найдено')

def delete(mycontacts):
    name = input('Введите имя')
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена')
    else:
        print('Это имя не найдено')

def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')
    pickle.dump(mycontacts, output_file)
    output_file.close()
main()



