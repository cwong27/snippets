class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for c in s:
            if c in dict.keys():
                dict[c] += 1
            else:
                dict[c] = 1
        for i, c in enumerate(s):
            if dict[c] == 1:
                return i
        return -1