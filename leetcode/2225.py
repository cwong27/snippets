class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        for m in matches:
            loser = str(m[1])
            winner = str(m[0])
            if winner not in loses.keys():
                loses[winner] = 0
            if loser in loses.keys():
                loses[loser] += 1
            else:
                loses[loser] = 1
        zero_lose = []
        one_lose = []
        
        for key, value in loses.items():
            if value == 0:
                zero_lose.append(int(key))
            elif value == 1:
                one_lose.append(int(key))
        res = []
        zero_lose.sort()
        one_lose.sort()
        res.append(zero_lose)
        res.append(one_lose)
        return res
            