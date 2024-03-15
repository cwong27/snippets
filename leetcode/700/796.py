class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        l = len(s)
        for i in range(l):
            if s[0] == goal[i]:
                start = i
                for j in range(l):
                    if s[j] != goal[(start+j)%l]:
                        break
                    if j == len(s)-1:
                        return True
        return False