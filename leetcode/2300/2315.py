class Solution:
    def countAsterisks(self, s: str) -> int:
        count = True
        res = 0
        for c in s:
            if c == '*' and count: res += 1
            if c == '|': count = not count
        return res