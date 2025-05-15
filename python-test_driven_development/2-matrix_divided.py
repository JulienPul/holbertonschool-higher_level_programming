#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance (div,(int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance (matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
