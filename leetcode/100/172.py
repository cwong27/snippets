class Solution:
    def trailingZeroes(n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
        
print(Solution.trailingZeroes(5))