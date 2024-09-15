class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h = heights.copy()
        heights.sort()
        res = 0
        for i, v in enumerate(heights):
            if v != h[i]:
                res +=1
        return res