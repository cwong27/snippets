class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                pre += nums[i]
            else:
                break
        result = nums[0]
        for n in range(pre , 100000):
            if n not in nums:
                result = n
                break
        return result