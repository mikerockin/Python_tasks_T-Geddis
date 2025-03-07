five_cop = (int(input('Введите количество 5 копеешных монет')))*5
ten_cop = (int(input('Введите количество 10 копеешных монет')))*10
fift_cop = (int(input('Введите количество 50 копеешных монет')))*50
sum = five_cop + ten_cop + fift_cop
if sum == 100:
    print('Вы выиграли')
elif sum > 100:
    print('Cумма больше необходимого числа', sum)
elif sum < 100:
    print('Cумма меньше необходимого числа', sum)
