class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = 0
        for i in range(0, (len(words)//2) +1):
            if words[(startIndex + i)%len(words)] == target or words[startIndex - i] == target: return res
            else: res += 1
        return -1