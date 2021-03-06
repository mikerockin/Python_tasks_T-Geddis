def main():
    file_1 = open('text.txt', 'r')
    text_1 = file_1.read()
    words_1 = text_1.split()
    unique_words_1 = set(words_1)
    file_2 = open('text2.txt', 'r')
    text_2 = file_2.read()
    words_2 = text_2.split()
    unique_words_2 = set(words_2)
    print('Список уникальных слов файла № 1: ', unique_words_1)
    print('Список уникальных слов файла № 2: ', unique_words_2)
    print('Список слов входящих в оба файла: ', unique_words_1.intersection(unique_words_2))
    print('Список слов из первого файла не входящих во второй: ', unique_words_1.difference(unique_words_2))
    print('Список слов из второго файла не входящих в первый: ', unique_words_2.difference(unique_words_1))
    print('Список слов входяих либо в первый файл, либо во второй, не входящие в оба одновременно ', unique_words_1.symmetric_difference(unique_words_2))
main()
