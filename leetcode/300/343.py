class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        return max((3**(n//3))*(1 if n % 3 == 0 else n % 3), 4*(3**((n-4)//3)))