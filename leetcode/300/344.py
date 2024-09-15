class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        swap = ""
        for i in range(int(l/2)):
            swap = s[l-1-i]
            s[l-1-i] = s[i]
            s[i] = swap 
        