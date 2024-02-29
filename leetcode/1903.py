class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i, c in enumerate(reversed(num)):
            if int(c)%2 != 0:
                return num[:len(num)-i]
        return ""
