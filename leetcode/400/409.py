class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        res = 0
        for c in s:
            if c not in counts.keys():
                counts[c] = 1
            else:
                if counts[c] == 1:
                    res += 2
                    counts[c] = 0
                else:
                    counts[c] = 1
        if res < len(s):
            res += 1
        return res