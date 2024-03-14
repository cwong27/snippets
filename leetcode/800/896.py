def isMonotonic(nums) -> bool:
    inc, dcr = True, True
    if len(nums) == 1: return True
    cur, next = nums[0], nums[1]
    for i in range(0,len(nums)-1):
        cur, next = nums[i], nums[i+1]
        if cur < next: dcr = False
        if cur > next: inc = False
    return inc or dcr

print(isMonotonic([1,3,2]))