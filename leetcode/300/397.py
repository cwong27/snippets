class Solution:
    def integerReplacement(n) -> int:
        if n == 1: return 0
        res = [0]*(n+1)
        res[1] = 0
        res[2] = 1
        for i in range(3,n+1):
            if i%2 == 0:
                res[i] = res[i//2]+1
            else:
                res[i] = min(res[(i+1)//2], res[(i-1)//2]) + 2
        return res[n]

print(Solution.integerReplacement(100000000))