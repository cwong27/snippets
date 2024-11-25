class Solution:
    def compressedString(self, word: str) -> str:
        cur_c, cur_count = '', 0
        comp = ""
        for c in word:
            if c != cur_c:
                comp += str(cur_count)+cur_c
                cur_c = c
                cur_count = 1
            else:
                cur_count += 1
                if cur_count == 10:
                    comp += "9"+cur_c
                    cur_count = 1
        comp += str(cur_count)+cur_c
        return comp[1:]