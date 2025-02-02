class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if i == j or n-i == j+1  : 
                    if grid[i][j] == 0: return False
                elif grid[i][j] != 0: return False
        return True