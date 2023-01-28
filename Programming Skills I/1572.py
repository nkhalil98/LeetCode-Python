"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""

def diagonalSum(mat: list[list[int]]) -> int:
        n = len(mat)
        diag_sum = 0
        for i in range(n):
            diag_sum += mat[i][i]
            diag_sum += mat[i][n-1-i]
        if n%2 == 1:
            diag_sum -= mat[n//2][n//2]
        return diag_sum

if __name__ == "__main__":
    # test cases
    assert diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]) == 25
    assert diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]) == 8
    assert diagonalSum([[5]]) == 5