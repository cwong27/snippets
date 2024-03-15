class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        left, right = 0, sum(nums[1:])
        for i in range(0, len(nums)):
            if left == right:
                return i
            left += nums[i]
            if i == len(nums)-1:
                right = 0
            else:
                right -= nums[i+1]
        return -1
