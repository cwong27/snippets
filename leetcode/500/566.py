class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (r*c) != (len(mat)*len(mat[0])): return mat
        res = [[0 for _ in range(c)] for _ in range(r)]
        row, col = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col == c:
                    row += 1
                    col = 0
                res[row][col] = mat[i][j]
                col += 1
        return res