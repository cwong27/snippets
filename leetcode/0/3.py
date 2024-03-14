class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest = 1
        for i, v1 in enumerate(s):
            char = set()
            char.add(v1)
            for j, v2 in enumerate(s[i+1:]):
                if v2 not in char:
                    char.add(v2)
                    if len(char) > longest:
                        longest = len(char)
                else:
                    break
            char.clear()
        return longest