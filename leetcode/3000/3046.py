class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        s = set(nums)
        for c in s:
            if nums.count(c) >= 3:
                return False
        return True