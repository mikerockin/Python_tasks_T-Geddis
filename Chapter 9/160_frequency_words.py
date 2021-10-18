def main():
    counter = {}
    infile = open('text.txt', 'r')
    text = infile.read()
    words = text.split()
    unique_words = set(words)
    for word in unique_words:
        counter[word] = 0
    for item in words:
        counter[item] +=1
        # Показать результаты
    print(format('слово', '15'), '\t', format('появления', '15'))
    print('----------------------------------------------')
    while len(counter) > 0:
        pair = counter.popitem()
        print(format(pair[0], '15'), format(pair[1], '15'))

main()
