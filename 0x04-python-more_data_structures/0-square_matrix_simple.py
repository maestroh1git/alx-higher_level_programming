#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_array = []
    if not matrix:
        pass

    for i in matrix:
        r = map(lambda x: x**2, i)
        new_array.append(list(r))
    return new_array
