class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        min  = n+1
        for i in range(n):
            curr = (start+i)%n
            if nums[curr] == target and abs(curr-start) < min:
                min = abs(curr-start)
        return min