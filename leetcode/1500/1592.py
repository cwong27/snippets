class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        w, s = len(words), text.count(' ')
        if w>1:
            n, r = s//(w-1), s%(w-1) 
            return (' '*n).join(words) + ' '*r
        else:
            return words[0] + ' '*s