class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        l = len(words)
        for i, word in enumerate(words):
            next = ""
            if i == l-1:
                next = words[0]
            else:
                next = words[i+1]
            if word[-1] != next[0]:
                return False
        return True