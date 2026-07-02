class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height, max = 0, 0
        for i, v in enumerate(gain):
            height += v
            if height > max: max = height
        return max