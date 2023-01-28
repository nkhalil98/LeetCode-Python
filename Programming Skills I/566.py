"""
566. Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""

def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        if r*c != m*n:
            return mat
        data = [e for row in mat for e in row]
        new_mat = []
        new_row = []
        for e in data:
            new_row.append(e)
            if len(new_row)==c:
                new_mat.append(new_row)
                new_row = []
        return new_mat

if __name__ == "__main__":
    # test cases
    assert matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]
    assert matrixReshape([[1,2],[3,4]], 2, 4) == [[1,2],[3,4]]        