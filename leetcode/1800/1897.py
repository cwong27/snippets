class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        l = len(words)
        for word in words:
            for c in word:
                if str(c) in counts.keys():
                    counts[str(c)] += 1
                else:
                    counts[str(c)] = 1
        for key,count in counts.items():
            if count % l != 0:
                return False
        return True 