class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_ = 0
        for i in range(len(nums)-1):
            max_ = max(max_, abs(nums[i]-nums[i+1]))
        max_ = max(max_, abs(nums[0]-nums[-1]))
        return max_