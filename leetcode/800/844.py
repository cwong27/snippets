class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = "",""
        for c in s:
            if c != '#':
                s1 += c
            else:
                s1 = s1[:-1]
        for c in t:
            if c != '#':
                s2 += c
            else:
                s2 = s2[:-1]
        return s1 == s2