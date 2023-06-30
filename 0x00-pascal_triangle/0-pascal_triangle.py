#!/usr/bin/python3
"""Create pascal triangle function"""


def pascal_triangle(n):
    """
        function to return an array of array of pascal triangle
    """
    triangle = []
    for row in range(n):
        triRow = []
        for col in range(row+1):
            if col == 0 or col == row:
                element = 1
            else:
                element = triangle[row-1][col-1] + triangle[row-1][col]
            triRow.append(element)
        triangle.append(triRow)
    return triangle
