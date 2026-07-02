class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            weight = 0
            for c in word:
                weight += weights[ord(c)-97]
            weight = weight%26
            res += chr(97+25-weight)
        return res