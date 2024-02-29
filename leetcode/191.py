class Solution:
    def hammingWeight(self, n: int) -> int:
        b = "{0:b}".format(n)
        count = 0
        for c in b:
            if c == '1':
                count += 1
        return count