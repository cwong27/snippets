class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuple_list = []
        for i,v in enumerate(names):
            tuple_list.append((v,heights[i]))
        sorted_list = sorted(tuple_list, key=lambda x: x[1])
        res = []
        for e in sorted_list:
            res.append(e[0])
        return res[::-1]