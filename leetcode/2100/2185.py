class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res, l = 0, len(pref)
        for word in words:
            if word[:l] == pref:
                res += 1
        return res