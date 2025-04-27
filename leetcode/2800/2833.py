class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, b = moves.count('L'), moves.count('R'), moves.count('_')
        if l == r: return b
        return abs(l-r)+b