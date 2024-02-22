class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = [0]*(len(nums)+1)
        dup = -1
        for i in nums:
            if n[i] != 0:
                dup = i
            else: 
                n[i] = i
        for i in range(1, len(nums)+1):
            if n[i] == 0:
                return [dup,i]
        