seconds_man = int(input('Введите количество секунд'))
days = seconds_man // 86400
hours = seconds_man // 3600
minutes = seconds_man // 60
sec_r = seconds_man - minutes * 60
min_r = (seconds_man - hours * 3600) // 60
hours_r = (seconds_man - days * 86400) // 3600
if seconds_man >= 60 and seconds_man < 3600:
    print(minutes, 'минут', sec_r, 'секунд')
elif seconds_man >= 3600 and seconds_man <86400:
    print(hours, 'часов', min_r, 'минут', sec_r, 'секунд')
elif seconds_man >= 86400:
    print(days, 'дней', hours_r, 'часов', min_r, 'минут', sec_r, 'секунд')