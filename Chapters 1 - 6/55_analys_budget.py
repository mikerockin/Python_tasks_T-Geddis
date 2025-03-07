max = int(input('Введите сумму выделенную на 1 месяц : '))
total = 0
for x in range (5):
    expenses = int(input('Введите сумму статьи расхода : '))
    total += expenses
print('Сумарные транты составили :',total)
xxx = max - total
if xxx > 0:
    print('Вы сэкономили: ', xxx)
elif xxx == 0:
    print('Вы уложились в заданную сумму!')
elif xxx < 0:
    xxx *= -1
    print('Перерасход составил: ', xxx)