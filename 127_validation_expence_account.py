def main():
    infile = open('expence_account_txt', 'r')
    list = infile.readlines()
    infile.close()
    index = 0
    found_user = input('Введите номер счета: ')
    while index < len(list):
        list[index] = list[index].rstrip('\n')
        index += 1
    if found_user in list:
        print('Есть такая буква в этом слове ')
    else:
        print('Указанный номер счета отсутствует в списке')
main()