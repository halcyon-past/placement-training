def twosum(nums,target):
    l = 0
    r = len(nums)-1
    while l<r:
        if nums[l] + nums[r] == target:
            return [l,r]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return [-1,-1]

nums = [1,2,3,4,5,6,7,8,9]
target = 10
print(twosum(nums,target))