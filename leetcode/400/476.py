class Solution:
    def findComplement(self, num: int) -> int:
        b = "{0:b}".format(num)
        bc = ""
        for c in b:
            if c == '0':
                bc += '1'
            elif c == '1':
                bc += '0'
        return int(bc, 2)