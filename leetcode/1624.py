class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_set = set()
        max = -1
        for c in s:
            if s.count(c) > 1:
                char_set.add(c)
        for c in char_set:
            i, j = 0, len(s)-1
            left = right = False
            while i < j:
                if s[i] != c:
                    i += 1
                else: 
                    left = True
                if s[j] != c:
                    j -= 1
                else:
                    right = True
                if left and right:
                    break
            if len(s[i+1:j]) > max:
                max = len(s[i+1:j])
        return max