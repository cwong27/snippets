class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odds, evens = 0, 0
        for n in nums:
            if n % 2 == 0:
                evens += 1
            else:
                odds +=1
        return [0]*evens + [1]*odds