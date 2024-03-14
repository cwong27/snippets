def subarraySum(nums, k):
    res = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)+1):
            d = nums[i:j]
            if sum(nums[i:j]) == k:
                res += 1
    return res
subarraySum([1,2,3], 3)