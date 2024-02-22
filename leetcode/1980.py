class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        for i,n, in enumerate(nums):
            if n[i] == "0":
                res += "1"
            else:
                res += "0"
        return res
        