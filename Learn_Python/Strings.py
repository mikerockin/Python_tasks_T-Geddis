# -*- coding: utf8 -*-
# Строки
# Изменение регистра символов в строках.
print('1.')
name = 'ada lovelace'
print(name.title())
print(name.lower())
print(name.upper())
print()
# Использование переменных в строках

print('2.')
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}' # Вставили значение переменной в строку, f строки появились в Python 3.6
message = f'Hello, {full_name.title()}!'
print(message)
# Табуляция
# \n - новая строка
# \t - табуляция

# Удаление пропусков

# rstrip

# Множественные присваивания

x,y,z = 1,2,3
print(x)