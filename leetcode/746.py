class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mcost = cost
        for i in range(2, len(cost)):
            mcost[i] = min(mcost[i]+cost[i-1], mcost[i]+cost[i-2])
        return min(mcost[len(cost)-1],mcost[len(cost)-2])