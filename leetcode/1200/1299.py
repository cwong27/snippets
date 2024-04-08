class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr)-2, 0, -1):
            cur = arr[i]
            arr[i] = mx
            mx = max(mx, cur)
        arr[0] = mx
        arr[-1] = -1
        return arr