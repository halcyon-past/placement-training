"""
Given an array of number where only one number is not repeated twice, find the number that is not repeated twice.
Example:
Input: [1,2,2,3,3,4,4]
Output: 1
"""

def findNonRepeated(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

nums = [1,2,2,3,3,4,4]
print(findNonRepeated(nums))

# Time Complexity: O(n)