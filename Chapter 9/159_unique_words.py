def main():
    infile = open('text.txt', 'r')
    text = infile.read()
    words = text.split()
    unique_words = set(words)
    for word in unique_words:
        print(word)
    infile.close()
main()