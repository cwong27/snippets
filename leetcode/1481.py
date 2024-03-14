class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        element_counts = Counter(arr)
        elements = len(element_counts)
        sorted_counts = sorted(element_counts.items(), key=lambda x: x[1])
        for n in sorted_counts:
            if n[1] <= k:
                k -= n[1]
                elements -= 1
            else:
                return elements
        return 0