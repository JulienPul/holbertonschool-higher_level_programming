#!/usr/bin/python3
"""
2-matrix_divided module

Defines a function matrix_divided(matrix, div) that divides all elements
of a matrix by a divisor and returns a new matrix with results rounded
to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Returns:
        list of lists of floats: New matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or rows are not of the same size,
                   or div is not a number.
        ZeroDivisionError: If div is 0.
    """
  
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if (not isinstance(matrix, list) or matrix == [] or
       any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
