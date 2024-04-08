class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            prd = 1
            for j in range(i, len(nums)):
                prd *= nums[j]
                if prd < k:
                    res += 1
                else:
                    break
        return res