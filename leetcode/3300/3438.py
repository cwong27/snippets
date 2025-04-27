class Solution:
    def findValidPair(self, s: str) -> str:
        counter = collections.Counter(s)
        for i,c in enumerate(s[:-1]):
            if counter[c] == int(c) and counter[s[i+1]] == int(s[i+1]) and c != s[i+1]:
                return c+s[i+1]
        return ""