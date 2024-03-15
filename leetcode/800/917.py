class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) == 1: return s
        i, j = 0, len(s)-1
        res = [""]*len(s)
        while i <= j:
            if s[i].isalpha() and s[j].isalpha():
                res[i] = s[j]
                res[j] = s[i]
                i += 1
                j -= 1
            if not s[i].isalpha():
                res[i] = s[i]
                i += 1
            if not s[j].isalpha():
                res[j] = s[j]
                j -= 1
        return ''.join(res)