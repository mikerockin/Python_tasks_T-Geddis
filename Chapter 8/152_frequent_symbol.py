def main():
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    index = 0
    frequent = 0
    user_string = input('Введите строковое значение: ')
    for ch in user_string:
        ch = ch.upper()
        index = letters.find(ch)
        if index>=0:
            count[index] = count[index] + 1
    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i
    print('Самый частый символ в строковом значении: ', \
          letters[frequent], '.', sep='')
main()
