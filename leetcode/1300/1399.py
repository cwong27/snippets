class Solution:
    def countLargestGroup(self, n: int) -> int:
        def getSum(n): 
            strr = str(n)
            list_of_number = list(map(int, strr.strip()))
            return str(sum(list_of_number))
        sums = {}
        largest = 0
        for n in range(1, n+1):
            k = getSum(n)
            if k not in sums.keys():
                sums[k] = 1
            else:
                sums[k] += 1
            largest = max(largest, sums[getSum(n)])
        res = 0
        for val in sums.values():
            if val == largest: res += 1
        return res