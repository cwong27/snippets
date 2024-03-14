class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_ = -1
        for i in range(0, len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                max_ = max(max_, int(num[i]))
        if max_ >= 0:
            return str(max_)*3
        return ""