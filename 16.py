R = int(input('Введите длину гряды в метрах: '))
Е = int(input('Введите размер пространства занимаемого концевыми опорами в метрах: '))
S = int(input('Введите размер пространства между виноградными лозами в метрах: '))
V = (R - 2 * Е) / S
print(V)