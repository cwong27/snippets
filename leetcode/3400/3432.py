class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        left, right = nums[0], sum(nums[1:])
        for i,v in enumerate(nums[1:]):
            left += v
            right -= v
            if abs(left-right)%2==0: res += 1
        return res