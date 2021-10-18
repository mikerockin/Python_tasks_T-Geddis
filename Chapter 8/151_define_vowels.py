def main ():
    vowels = 0
    consonants = 0
    user_words = input('Введите строковое значение. а я покажу вам количество глассных и согласных букв в нем: ')
    vowels = vowels_counter(user_words)
    consonants = consonants_counter(user_words)
    print('Введенное строковое значение содержит', vowels, \
          'гласных и', consonants, 'согласных.')

def vowels_counter(user_words):
    count = 0
    vowels = 'аеёиоуыэюя'
    for ch in user_words:
        if vowels.find(ch)>=0:
            count +=1
    return count

def consonants_counter(user_words):
    count = 0
    consonants = 'бвгджзйклмнпрстфхцчшщъь'
    for ch in user_words:
        if consonants.find(ch)>=0:
            count +=1
    return count

main()

