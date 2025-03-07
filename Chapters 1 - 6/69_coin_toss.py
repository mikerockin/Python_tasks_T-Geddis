import random

HEADS = 1
TAILS = 2
TOSSES = 1

def main():
    for toss in range (TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print ('Решка')
main()