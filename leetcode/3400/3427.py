class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sum_ = 0 
        for i in range(len(nums)):
            sum_ += sum(nums[max(0,i-nums[i]):i+1])
        return sum_