# Упражнение по программированию 9-5

# Частотность слов

def main():
    # Задать пустой словарь
    counter = {}

    # Файл находится в подпапке data
    input_file = open('text.txt','r')

    text = input_file.read()
    words = text.split()

    # Добавить каждое уникальное слово в словарь со счетчиком 0
    unique_words = set(words)
    for word in unique_words:
        counter[word] = 0

    # По каждому слову в тексте увеличить его счетчик в словаре
    for item in words:
        counter[item] += 1

    # Показать результаты
    print(format('слово', '20'), '\t', format('появления', '20'))
    print('----------------------------------------------')
    while len(counter) > 0:
        pair = counter.popitem()
        print(format(pair[0], '15'), format(pair[1], '15'))


# Вызвать главную функцию.
main()
