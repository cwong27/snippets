class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i,c in enumerate(s):
            res += (26-(ord(c)-97))*(i+1)
        return res
