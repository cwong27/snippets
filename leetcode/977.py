import heapq as heap
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        start, end = 0, n-1
        for i in range(n-1, -1, -1):
            if abs(nums[start]) >= abs(nums[end]):
                res[i] = nums[start]**2
                start += 1
            else:
                res[i] = nums[end]**2
                end -= 1
        return res