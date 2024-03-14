class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: return 1
        total = (n*(n+1))/2
        left, right = 1, total-1
        for i in range(2, n):
            left += i
            if left == right:
                return i
            right -= i
        return -1