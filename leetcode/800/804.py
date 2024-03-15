class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            m = ""
            for c in w:
                m += morse[ord(c)-97]
            res.add(m)
        return len(res)