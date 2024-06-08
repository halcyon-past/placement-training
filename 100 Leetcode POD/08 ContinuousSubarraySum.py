"""
523. Continuous Subarray Sum
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n<2: return False
        mod_k={}
        prefix=0
        mod_k[0]=-1
        for i, x in enumerate(nums):
            prefix+=x
            prefix%=k
            if prefix in mod_k:
                if i>mod_k[prefix]+1:
                    return True
            else:
                mod_k[prefix]=i
        return False

# Time Complexity: O(n)

# Test Cases

test = Solution()
assert test.checkSubarraySum([23,2,4,6,7],6) == True
assert test.checkSubarraySum([23,2,6,4,7],6) == True
assert test.checkSubarraySum([23,2,6,4,7],13) == False

print("All Test Cases Passed")