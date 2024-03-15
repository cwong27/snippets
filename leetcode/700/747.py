class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m,n,index = 0, 0, 0
        for i in range(len(nums)):
            if m < nums[i]:
                m, n, index = nums[i], m, i
            if nums[i] > 0 and nums[i] < m and nums[i] > n:
                n = nums[i]
        if m >= n*2:
            return index
        return -1