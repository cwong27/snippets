class Solution:
    def findLucky(self, arr: List[int]) -> int:
        largest = -1
        count = {}
        for n in arr:
            if str(n) in count:
                count[str(n)] += 1
            else:
                count[str(n)] = 1
        for n in count.keys():
            if count[n] == int(n):
                largest = max(int(n),largest)
        return largest