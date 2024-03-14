class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr)//4
        for i in arr:
            c = arr.count(i)
            if quarter < c:
                return i