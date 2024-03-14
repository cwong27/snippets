class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        next_cookie = 0
        g.sort()
        s.sort()
        for i in range(0, len(g)):
            for j in range(next_cookie, len(s)):
                if s[j] >= g[i]:
                    count += 1
                    next_cookie = j+1
                    break
        return count