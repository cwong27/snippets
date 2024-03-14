class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sa = set(ransomNote)
        for c in sa:
            if magazine.count(c) < ransomNote.count(c):
                return False
        return True