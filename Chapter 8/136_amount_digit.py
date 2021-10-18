mystring = '1213'
counter = 0
for ch in mystring:
    if ch.isdigit():
        counter +=1
print('Количествоы цифр равно', counter)