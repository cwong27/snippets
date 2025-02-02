class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    res += 'o'
                    i = i+2
                else:
                    res += 'al'
                    i = i+4
        return res