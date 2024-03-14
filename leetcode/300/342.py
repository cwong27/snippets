class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        f = 1
        while n >= f:
            if n^f == 0:
                return True
            f = f << 2
        return False