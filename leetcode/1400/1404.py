class Solution:
    def numSteps(self, s: str) -> int:
        step = 0
        n = int(s, 2)
        while n != 1:
            if n%2 == 0:
                n = n >> 1
            else:
                n += 1
            step += 1
        return step