def main ():
    print('Эта программа конвертирует футы в дюймы')
    feet_to_inch = int(input('Введите футы для конвертации: '))
    inches = feet_to_inches(feet_to_inch)
    print('В', feet_to_inch, 'футов, содержится: ', inches, 'дюймов')
def feet_to_inches(feet):
    inches = feet * 12
    return inches
main()
