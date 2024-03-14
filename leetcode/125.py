class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub(r'\W+', '', s)
        s1 = s1.replace("_", "")
        s1 = s1.lower()
        return s1 == s1[::-1]