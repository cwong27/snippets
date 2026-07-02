class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = 2 ** 32
        for n in nums:
            cur = sum(int(digit) for digit in str(n))
            if cur < res: res = cur
        return res