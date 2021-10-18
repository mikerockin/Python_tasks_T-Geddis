def main():
    upper = 0
    lower = 0
    space = 0
    digits = 0
    infile = open('text.txt', 'r')
    data = infile.read()
    for item in data:
        if item.isupper():
            upper += 1
        if item.islower():
            lower += 1
        if item.isdigit():
            digits += 1
        if item.isspace():
            space += 1
    infile.close()
    print('Количество букв в верхнем регистре : ', upper)
    print('Количество букв в нижнем регистре : ', lower)
    print('Количество цифр : ', digits)
    print('Количество пробелов : ', space)

main()