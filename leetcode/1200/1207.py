class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set(arr)
        counts = set()
        for n in s:
            count = arr.count(n)
            if count in counts:
                return False
            else:
                counts.add(count)
        return True