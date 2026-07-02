class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, upper = set(), set()
        res = 0
        for c in word:
             if c.islower(): lower.add(c)
             if c.isupper(): upper.add(c)
        for c in lower:
            if c.upper() in upper: res += 1
        return res