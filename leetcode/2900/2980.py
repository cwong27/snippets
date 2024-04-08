class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evens = 0
        for n in nums:
            if n%2 == 0:
                evens += 1
                if evens == 2:
                    return True
        return False