class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        l = len(cost)
        total = 0
        for i in range(0, l, 3):
            if i+2 > l:
                total += cost[i]
                if i+1 == l-1: total += cost[i+1]
            else:
                total += (cost[i]+cost[i+1])
        return total