class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        s = sorted(nums[1:])
        return cost + s[0] + s[1]