class Solution:
    def isThree(n: int) -> bool:
        if n == 1 or n == 2:
            return False
        count = 2
        for i in range(2, n//2+1):
            if n%i == 0:
                count += 1
            if count > 3:
                return False
        if count == 3:
            return True
        return False

print(Solution.isThree(4))