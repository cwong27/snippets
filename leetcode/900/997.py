class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_dg = [0]*(n+1)
        out_dg = [0]*(n+1)
        for t in trust:
            out_dg[t[0]] += 1
            in_dg[t[1]] += 1
        for i in range(1, n+1):
            if in_dg[i] == n-1 and out_dg[i] == 0:
                return i
        return -1
        