"""
862. Shortest Subarray with Sum at Least K
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
"""

from itertools import accumulate
from typing import List
import operator

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums=list(accumulate(nums, operator.add))

        dp=[0]*n
        front, back, Len=0, -1, 10**9
        for r, x in enumerate(nums):
            if x>=k: Len=min(Len, r+1)
            while front<=back and x-nums[dp[front]]>=k:
                Len=min(Len, r-dp[front])
                front+=1
            while front<=back and x<=nums[dp[back]]:
                back-=1
            back+=1
            dp[back]=r
        return Len if Len!=10**9 else -1

# Test cases

test = Solution()
assert test.shortestSubarray([1], 1) == 1
assert test.shortestSubarray([1,2], 4) == -1
assert test.shortestSubarray([2,-1,2], 3) == 3

print("All tests passed")