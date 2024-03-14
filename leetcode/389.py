class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = set(t)
        for c in ss:
            if s.count(c) != t.count(c):
                return str(c)