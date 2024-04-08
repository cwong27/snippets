class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)
        res = [0,0]
        for i in range(len(nums1)):
            if nums1[i] in s2:
                res[0] += 1
        for i in range(len(nums2)):
            if nums2[i] in s1:
                res[1] += 1
        return res