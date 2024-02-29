class Solution:
    def minOperations(self, nums: List[int]) -> int:
        unique = Counter(nums)
        ops = 0
        for n in unique.values():
            if n == 1:
                return -1
            if n % 3 == 0:
                ops += n//3
            else:
                ops += n//3 + 1
        return ops