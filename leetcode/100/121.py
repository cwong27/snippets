class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, max_p = prices[0], 0
        for n in prices:
            lowest = min(n, lowest)
            max_p = max(max_p, n-lowest)
        return max_p