class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bits = "{0:b}".format(n)
        ones = False
        if n <= 0:
            return False
        for n in bits:
            if n == "1":
                ones += 1
                if ones > 1:
                    return False
        return True