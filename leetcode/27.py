class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                res += 1
            else:
                for j in range(len(nums[i:])):
                    if nums[i+j] != val:
                        nums[i] = nums[i+j]
                        nums[i+j] = val
                        res += 1
                        break
        return res