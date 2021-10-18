digit_list = ['2','3','4','5','6','7','8','9']
alpha_phone_number = ''
num_phone_number = ''
user_number = input('Введите номер телефона в формате XXX-XXX-XXXX: ')
print(user_number)
for us_ph in user_number:
    if us_ph.isalpha():
        us_ph = us_ph.upper()
        if us_ph == 'A' or us_ph == 'B' or us_ph == 'C':
            index = 0
        elif us_ph == 'D'or us_ph == 'E' or us_ph == 'F':
            index = 1
        elif us_ph == 'G' or us_ph == 'H' or us_ph == 'I':
            index = 2
        elif us_ph == 'J' or us_ph == 'K' or us_ph == 'l':
            index = 3
        elif us_ph == 'M' or us_ph == 'N' or us_ph == 'O':
            index = 4
        elif us_ph == 'P' or us_ph == 'Q'or us_ph == 'R' or us_ph == 'S':
            index = 5
        elif us_ph == 'T' or us_ph == 'U' or us_ph == 'V':
             index = 6
        elif us_ph == 'W' or us_ph == 'X' or us_ph == 'Y' or us_ph == 'Z':
            index = 7
        us_ph = digit_list[index]
    num_phone_number = num_phone_number + us_ph
print('Телефонный номер:', num_phone_number)


