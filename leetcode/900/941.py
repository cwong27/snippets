class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        if arr[0] >= arr[1]: return False
        inc = True
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]: return False
            if inc:
                if arr[i] > arr[i+1]: inc = False
            else:
                if arr[i] < arr[i+1]: return False
        return not inc