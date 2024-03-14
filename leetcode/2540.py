class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if nums1[i] == nums2[j]: return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
                if i == len(nums1): break
            if nums1[i] > nums2[j]:
                j += 1
                if j == len(nums2): break
        return -1