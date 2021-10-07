def main():
    boys_names_list = ''
    girls_names_list = ''
    infile_girls = open('GirlNames.txt', 'r')
    girls_names_list = infile_girls.readlines()
    for i in range(len(girls_names_list)):
        girls_names_list[i] = girls_names_list[i].rstrip('\n')
    infile_boys = open('BoyNames.txt', 'r')
    boys_names_list = infile_boys.readlines()
    for i in range(len(boys_names_list)):
        boys_names_list[i] = boys_names_list[i].rstrip('\n')
    user_name_boy = input('Введите мужское имя, если не хотите вводить мужское имя введите "Н" ' )
    user_name_girl = input('Введите женское имя, если не хотите вводить женское имя введите "Н" ' )
    if user_name_boy == 'Н':
        print('Вы решили не вводить мужское имя')
    elif user_name_boy in boys_names_list:
        print('Ваше имя находится в списке самых популярных мужских имен в Мире')
    else:
        print('Ваше имя довольно редкое')
    if user_name_girl == 'Н':
        print('Вы решили не вводить женское имя')
    elif user_name_boy in girls_names_list:
        print('Ваше имя находится в списке самых популярных женских имен в Мире')
    else:
        print('Ваше имя довольно редкое')
main()


