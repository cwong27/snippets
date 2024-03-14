class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        max_ = round(current / k, 5)
        for i in range(1,len(nums)-k+1):
            current = current - nums[i-1] + nums[i+k-1]
            max_ = max(max_, current/k)
        return max_