class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = Counter(list(moves))
        if counts['L'] != counts['R'] or counts['U'] != counts['D']:
            return False
        return True