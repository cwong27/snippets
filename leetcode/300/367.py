class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        n = 1
        while n**2 < num:
            n += 1
            if n**2 == num:
                return True
        return False