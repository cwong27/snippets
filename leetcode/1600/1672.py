class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _max = 0
        for i,v in enumerate(accounts):
            _max = max(sum(v), _max)
        return _max