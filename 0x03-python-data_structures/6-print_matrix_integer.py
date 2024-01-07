#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for element in range(len(matrix[row])):
                if element != len(matrix[row]) - 1:
                    space = ''
                else:
                    space = ""
                print("{:d}".format(matrix[row][element],end=space))
                print()
