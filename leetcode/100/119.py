class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        for i in range(1, rowIndex+1):
            res[i] = comb(rowIndex, i)
        return res