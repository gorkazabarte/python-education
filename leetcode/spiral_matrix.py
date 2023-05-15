"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

https://leetcode.com/problems/spiral-matrix-ii/

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 1
Output: [[1]]

1 <= n <= 20
"""

from numpy import zeros


def generate_matrix(n: int) -> list[list[int, ...]]:
    filler: int = 1
    matrix = zeros((n, n))
    left: int = 0
    right: int = n - 1
    top: int = 0
    bottom: int = n - 1

    while left <= right:
        filler = fill_upper(n, left, top, matrix, filler)
        filler = fill_right(n, right, top, matrix, filler)
        filler = fill_lower(n, right, bottom, matrix, filler)
        filler = fill_left(n, left, bottom, matrix, filler)

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return matrix


def fill_upper(n: int, left: int, top: int, matrix: list[list[int, ...]], filler: int) -> int:
    for i in range(left, n - left):
        matrix[top][i] = filler
        filler += 1
    return filler


def fill_right(n: int, right: int, top: int, matrix: list[list[int, ...]], filler: int) -> int:
    for i in range(top, n - top):
        if i != top:
            matrix[i][right] = filler
            filler += 1
    return filler


def fill_lower(n: int, right: int, bottom: int, matrix: list[list[int, ...]], filler: int) -> int:
    for i in range(right, -1 + (n - right - 1), -1):
        if i != bottom:
            matrix[bottom][i] = filler
            filler += 1
    return filler


def fill_left(n: int, left: int, bottom: int, matrix: list[list[int, ...]], filler: int) -> int:
    for i in range(bottom, -1 + left, -1):
        if i != left and i != bottom:
            matrix[i][left] = filler
            filler += 1
    return filler


if __name__ == '__main__':
    print(generate_matrix(7))
