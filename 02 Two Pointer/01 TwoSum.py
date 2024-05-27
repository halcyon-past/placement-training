"""
Given an array and a target value, return the indices of two numbers that add up to the target value.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""



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