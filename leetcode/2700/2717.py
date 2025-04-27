class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 1 and nums[n-1] == n: return 0
        one, nth = 0, 0
        for i, num in enumerate(nums):
            if num == 1: one = i
            if num == n: nth = i
        res = one+(n-nth-1)
        if one > nth: res -= 1
        return res