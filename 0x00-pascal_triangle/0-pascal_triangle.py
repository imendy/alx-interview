#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    creating a Pascal's triangle with n rows
    """
    triangle = []
    if n <= 0:
        return triangle

    for k in range(1, n + 1):
        row = []
        C = 1
        for j in range(1, k + 1):
            row.append(C)
            C = C * (k - j) // j
        triangle.append(row)

    return triangle
