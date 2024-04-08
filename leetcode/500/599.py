class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least = len(list1) + len(list2)
        res = []
        for i, s1 in enumerate(list1):
            for j, s2 in enumerate(list2):
                if s1 == s2:
                    if i+j < least:
                        least = i+j
                        res = []
                        res.append(s1)
                    elif i+j == least:
                        res.append(s1)
        return res