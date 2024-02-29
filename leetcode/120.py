class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        t = len(triangle)
        for i,row in enumerate(triangle[::-1]):
            if i == t-1:
                continue
            for j in range(len(row)-1):
                triangle[t-i-2][j] += min(triangle[t-i-1][j], triangle[t-i-1][j+1])
        return triangle[0][0]
