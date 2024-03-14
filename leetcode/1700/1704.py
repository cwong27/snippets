class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = int(len(s)/2)
        left, right = s[0: mid], s[mid:]
        lc = rc = 0
        vow = ["a","e","i","o","u","A","E","I","O","U"]
        for c in left:
            for v in vow:
                lc += left.count(v)
        for c in right:
            for v in vow:
                rc += right.count(v)
        return lc == rc
