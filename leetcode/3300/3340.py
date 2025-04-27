class Solution:
    def isBalanced(self, num: str) -> bool:
        even, odd = 0, 0
        for i,c in enumerate(num):
            if i%2 == 0: even += int(c)
            else: odd += int(c)
        return even == odd