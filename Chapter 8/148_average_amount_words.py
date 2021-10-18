def main():
    num_sentences = 0
    total_words = 0
    average_words = 0
    words = []
    infile = open('text.txt', 'r')
    sentences = infile.readlines()
    num_sentences = len(sentences)
    for item in sentences:
        words = item.split()
        total_words += len(words)
        average_words = total_words / num_sentences
    print('Среднее количество слов в строке:', average_words)
main()