class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        for i,v in enumerate(nums):
            if i-k >= 0:
                if nums[i-k] >= v: continue
            if i+k < len(nums):
                if nums[i+k] >= v: continue
            res += v
        return res