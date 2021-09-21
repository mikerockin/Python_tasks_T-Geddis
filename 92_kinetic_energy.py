def main():
    mass = int(input('Введите массу тела в киллограммах: '))
    speed = int(input('Ввежите значение скорости в метрах с секунду: '))
    kin_energy = kinetic_energy(mass, speed)
    print('Кинетическая энергия составит: ', kin_energy)
def kinetic_energy(m, s):
    kin_energy = 1/2 * m * (s ** 2)
    return kin_energy
main()



