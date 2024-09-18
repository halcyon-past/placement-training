"""
179. Largest Number
Solved
Medium
Topics
Companies
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == '0':
            return '0'
        return ''.join(nums)

# Test Cases

test = Solution()
assert test.largestNumber([10,2]) == "210"
assert test.largestNumber([3,30,34,5,9]) == "9534330"
assert test.largestNumber([0,0]) == "0"

print("All passed")