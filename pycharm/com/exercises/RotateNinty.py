import unittest


def print_matrix(matrix):
    for row in matrix:
        print(row)


def rotate_matrix(matrix):
    print('Matrix before folding')
    print_matrix(matrix)

    row_length = len(matrix)
    column_length = len(matrix[0])


    for i in range(row_length//2):
        for j in range(column_length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[row_length-i-1][j]
            matrix[row_length-i-1][j] = temp

    print('Matrix after folding')
    print_matrix(matrix)

    for i in range(row_length):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    print('----------------------')
    print('Matrix after Transpose')
    print_matrix(matrix)


def rotate_matrix_v1(matrix):
    length = len(matrix)
    if length == 1:
        return matrix

    #Number levels is length -1
    for level in range(length // 2):
        for i in range(length-2*level-1):
            temp = matrix[level][level+i]
            matrix[level][level+i] = matrix[i+level][length-level-1]
            matrix[i+level][length-level-1] = matrix[length-level-1][length-i-1]
            matrix[length - level - 1][length - i - 1] = matrix[length-i-1][level]
            print(f' matrix[length-level-1][level+i] { matrix[length-level-1][level+i]} {length-level-1} , {level+i}')
            matrix[length - i - 1][level] = temp
            print(f'--------level {level}-------------')
            print(*matrix, sep='\n')
        print(f'--------level {level}-------------')
        print(*matrix, sep='\n')


def rotate_matrix_v2(matrix):
    length = len(matrix)
    if length == 1:
        return matrix

    #Number levels is length -1
    for i in range(0, length//2):
        for j in range(i, length - i -1):
            temp = matrix[i][j]

            matrix[i][j] = matrix[j][length-i-1]
            matrix[j][length-i-1] = matrix[length-i-1][length-j-1]
            matrix[length - i - 1][length - j - 1] = matrix[length - j - 1][i]
            matrix[length - j - 1][i] = temp

            print(f'[{i}][{j}]')
            print(f'[{j}][{length-i-1}]')
            print(f'[{length - i - 1}][{length - j - 1}]')
            print(f'[{length - j - 1}][{i}]')
            print(*matrix, sep='\n')

        print(f'--------level {i}-------------')
        print(*matrix, sep='\n')

        return matrix

class UnitTestClass(unittest.TestCase):

    def test_rotate_matrix_v2(self):
        matrix_1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        matrix_1_r = [
            [4, 8, 12, 16],
            [3, 7, 11, 8],
            [2, 6, 10, 12],
            [1, 5, 9, 13]
        ]

        matrix_2 = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]

        matrix_2_r = [
            [5, 10, 15, 20, 25],
            [4, 9, 14, 19, 24],
            [3, 8, 13, 18, 23],
            [2, 7, 12, 17, 22],
            [1, 22, 23, 24, 21],
        ]

        matrix_3 = [
            [1, 2],
            [3, 4]
        ]

        matrix_3_r = [
            [2, 4],
            [1, 3]
        ]

        test_cases = [(matrix_1, matrix_1_r),
                      (matrix_2, matrix_2_r),
                      (matrix_3, matrix_3_r)
                      ]

        for key, result in test_cases:
            self.assertTrue(rotate_matrix_v2(key), result)


if __name__ == '__main__':
    '''matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    matrix_1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]


    print_matrix(matrix_1)
    rotate_matrix_v2(matrix_1)

    print('----------------------')
    print('Matrix after Transpose')
    print(*matrix_1, sep='\n')'''

    if __name__ == '__main__':
        unittest.main()















