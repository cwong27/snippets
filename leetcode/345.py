class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        c = list(s)
        v = ['a','e','i','o','u','A','E','I','O','U']
        while i < j:
            while c[i] not in v:
                i += 1
                if i == len(s)-1: break
            while c[j] not in v and j > 0:
                j -= 1
                if j == 0: break
            if i >= j: break
            buf = c[i]
            c[i] = c[j]
            c[j] = buf
            i += 1
            j -= 1
        str1 = ""
        return str1.join(c)