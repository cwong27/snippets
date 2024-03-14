class Solution:
    def maxScore(self, s: str) -> int:
        max_ = 0
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            zeros, ones = 0, 0
            for c in left:
                if c == '0':
                    zeros += 1
            for c in right:
                if c == '1':
                    ones += 1
            max_ = max(max_, zeros+ones)
        return max_