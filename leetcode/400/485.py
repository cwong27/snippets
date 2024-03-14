class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        current = 0
        for n in nums:
            if n == 1:
                current += 1
                max_ = max(max_, current)
            elif n == 0:
                current = 0
        return max_