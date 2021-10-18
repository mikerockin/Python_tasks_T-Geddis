def main():
    user_string = input('Введите предложения строчными буквами, после чего программа преобразует первое слово каждого предложения с заглавной буквы: ')
    result = modification(user_string)

    print(result)

def modification(user_string):
    result = ''
    new_sentence = True
    result_word = ''

    words = user_string.split()
    for item in words:
        if new_sentence:
            result_word = item[0].upper() + item[1:]
        else:
            result_word = item

        result = result + result_word + ' '

        if item[-1] == '.' or item[-1] == '?' or item[-1] == '!':
            new_sentence = True
        else:
            new_sentence = False

    return result

main()
