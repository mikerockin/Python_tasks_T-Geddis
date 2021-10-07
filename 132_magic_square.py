def main():
    square = [[4,9,2],[3,5,7],[8,1,6]]
    magic_square(square)
def magic_square(square):
    sum_0 = sum(square[0])
    sum_2 = sum(square[1])
    sum_3 = sum(square[2])
    sum_00 = square[0][0] + square[1][0] + square[2][0]
    sum_01 = square[0][1] + square[1][1] + square[2][1]
    sum_02 = square[0][2] + square[1][2] + square[2][2]
    sum_10 = square[0][0] + square[1][1] + square[2][2]
    sum_20 = square[0][2] + square[1][1] + square[2][0]
    if sum_00 == sum_01 and sum_00 == sum_02 and sum_0 == sum_2 and sum_0 == sum_3 and sum_10 == sum_20:
        print('Магический квадрат!')
    else:
        print('Квадрат немагический')
main()

