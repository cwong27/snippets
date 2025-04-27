class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_list = list(set(nums))
        unique_list.sort()
        for n in unique_list.copy():
            if len(unique_list) >= 2 and n < 0:
                unique_list.remove(n)
        return sum(unique_list)