class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n, sign, i = 0, 0, 1, 0
        res = [0]*len(nums)
        while i < len(nums):
            if sign == 1:
                while nums[p] < 0:
                    p += 1
                res[i] = nums[p]
                p += 1
            else:
                while nums[n] >= 0:
                    n += 1
                res[i] = nums[n]
                n += 1
            i += 1
            sign *= -1
        return res