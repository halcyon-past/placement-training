"""
2563. Count the Number of Fair Pairs
Solved
Medium
Topics
Companies
Hint
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
"""

from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 1):
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            start = bisect.bisect_left(nums, min_val, i + 1, n)
            end = bisect.bisect_right(nums, max_val, i + 1, n) - 1
            if start <= end:
                count += end - start + 1
        
        return count

# Test Cases

test = Solution()
assert test.countFairPairs([0,1,7,4,4,5], 3, 6) == 6
assert test.countFairPairs([1,7,9,2,5], 11, 11) == 1
assert test.countFairPairs([1,7,9,2,5], 1, 1) == 0

print("All tests passed")