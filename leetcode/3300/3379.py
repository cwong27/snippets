class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        for i,v in enumerate(nums):
            if v > 0:
                index = (i+v)%n
                result[i] = nums[index]
            elif v < 0:
                index = (i-abs(v))%n
                result[i] = nums[index]
            elif v == 0:
                result[i] = nums[i]
        return result