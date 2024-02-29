class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(nums):
            if len(nums) == 2:
                return True
            nums.sort()
            last = nums[0] - nums[1]
            for i in range(0, len(nums)-1):
                cur = nums[i] - nums[i+1]
                if last != cur:
                    return False
                last = cur
            return True
        m = len(l)
        res = []
        for i,v in enumerate(l):
            if isArith(nums[l[i]: r[i]+1]):
                res.append(True)
            else:
                res.append(False)
        return res