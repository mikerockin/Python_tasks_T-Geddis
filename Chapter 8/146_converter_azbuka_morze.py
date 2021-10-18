# Упражнение по программированию 8-4

# Конвертер азбуки Морзе

def main():
    # Локальные переменные
    morse_string = ''
    index = 0

    # Список кодов азбуки Морзе
    morse_list = [' ', '--..--', '.-.-.-', '-----',
                  '.----', '..---', '...--', '....-',
                  '.....', '-....', '--...', '---..',
                  '----.', '.-', '-...', '-.-.', '-..',
                  '.', '..-.', '--.', '....', '..', '.---',
                  '-.-', '.-..', '--', '-.', '---', '.--.',
                  '--.-', '.-.', '...', '-', '..-', '...-',
                  '.--', '-..-', '-.-', '--..']

    # Получить от пользователя строковое значение.
    morse_string = input('Введите строковое значение ' \
                         'для конвертации в коды азбуки Морзе: ')

    # Перебрать символы в строке, определить индекс кода
    # азбуки Морзе в списке и показать код для этого символа
    for ch in morse_string:
        # Преобразовать символ в верхний регистр.
        ch = ch.upper()

        # Определить индекс в списке.
        if ch == ' ':
            index = 0
        elif ch == ',':
            index = 1
        elif ch == '.':
            index = 2
        elif ch == '?':
            index = 3
        elif ch == '0':
            index = 4
        elif ch == '1':
            index = 5
        elif ch == '2':
            index = 6
        elif ch == '3':
            index = 7
        elif ch == '4':
            index = 8
        elif ch == '5':
            index = 9
        elif ch == '6':
            index = 10
        elif ch == '7':
            index = 11
        elif ch == '8':
            index = 12
        elif ch == '9':
            index = 13
        elif ch == 'A':
            index = 14
        elif ch == 'B':
            index = 15
        elif ch == 'C':
            index = 16
        elif ch == 'D':
            index = 17
        elif ch == 'E':
            index = 18
        elif ch == 'F':
            index = 19
        elif ch == 'G':
            index = 20
        elif ch == 'H':
            index = 21
        elif ch == 'I':
            index = 22
        elif ch == 'J':
            index = 23
        elif ch == 'K':
            index = 24
        elif ch == 'L':
            index = 25
        elif ch == 'M':
            index = 26
        elif ch == 'N':
            index = 27
        elif ch == 'O':
            index = 28
        elif ch == 'P':
            index = 29
        elif ch == 'Q':
            index = 30
        elif ch == 'R':
            index = 31
        elif ch == 'S':
            index = 32
        elif ch == 'T':
            index = 33
        elif ch == 'U':
            index = 34
        elif ch == 'V':
            index = 35
        elif ch == 'W':
            index = 36
        elif ch == 'X':
            index = 37
        elif ch == 'Y':
            index = 38
        elif ch == 'Z':
            index = 39

        # Показать коды азбуки Морзе для данного символа.
        print(morse_list[index], ',', sep='', end='')


# Вызвать главную функцию.
main()
