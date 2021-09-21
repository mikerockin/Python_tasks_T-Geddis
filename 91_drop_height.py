def main():
    for time in range (1, 10):
        distance = falling_distance(time)
        print('Расстояние составило', format(distance, ',.1f'), 'метров')
def falling_distance(time):
    g = 9.8
    distance = 1/2 * g * time
    return distance
main()