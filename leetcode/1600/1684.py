class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def consistent(string, allowed):
            s = list(string)
            for c in s:
                if c not in allowed:
                    return False
            return True

        res = 0
        for word in words:
            if consistent(word, allowed): res += 1
        return res
