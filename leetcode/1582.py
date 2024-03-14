class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    sp = True
                    for k,n in enumerate(mat[i]):
                        if n == 1 and k != j:
                            sp = False
                            break
                    for k in range(len(mat)):
                        if mat[k][j] == 1 and k != i:
                            sp = False
                            break
                    if sp:
                        count += 1
        return count
                    