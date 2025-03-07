amount_days = int(input('Enter numbers of days :'))
b = 1
print('Days\tSalary')
print('_____________')
total_salary = 0
for x in range(1, amount_days +1):
    b *= 2
    total_salary =  total_salary +  b
    print(x,'\t', b)
print('Заработная плата до вычета, за весь период в рублях', format((total_salary + b) / 100, ',.2f'))
print('Заработная плата до вычета, за весь период в копейках', total_salary)
print()
