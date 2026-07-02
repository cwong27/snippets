class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i,j = 0, len(colors)-1
        while i < j:
            if colors[i] != colors[j]: return j-i
            if colors[j] != colors[j-1]: return j-1
            if colors[i] != colors[i+1]: return len(colors)-i-2
            j -= 1
            i += 1