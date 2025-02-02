class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        dec = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                dec += 1
        if nums[0] < nums[-1]:
            dec += 1
        return not (dec >= 2) 