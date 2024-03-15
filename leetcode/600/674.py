class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        inc = [1]*len(nums)
        m = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc[i] += inc[i-1]
                m = max(inc[i], m)
        return m