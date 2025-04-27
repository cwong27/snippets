class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d, max_a = 0, 0
        for i,d in enumerate(dimensions):
            cur = math.sqrt(d[0]**2 + d[1]**2)
            if cur == max_d:
                if d[0]*d[1] > max_a:
                    max_d, max_a = cur, d[0]*d[1]
            elif cur > max_d:
                max_d, max_a = cur, d[0]*d[1]
        return max_a