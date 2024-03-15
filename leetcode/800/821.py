class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        index = []
        res = [0]*len(s)
        for i, ch in enumerate(s):
            if ch == c:
                index.append(i)
        for i, ch in enumerate(s):
            if ch == c: continue
            min_ = len(s)
            for d in index:
                min_ = min(min_, abs(d-i))
            res[i] = min_
        return res