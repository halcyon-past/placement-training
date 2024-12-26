"""
494. Target Sum
Solved
Medium
Topics
Companies
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        Sum=sum(nums)
        diff=Sum-target

        if diff<0 or diff%2==1: return 0
        diff/=2
        
        @cache
        def f(j , sum):
            if j==0: return 1 if sum==0 else 0
            x=nums[j-1]
            ans=f(j-1, sum)
            if sum>=x:
                ans+=f(j-1, sum-x)
            return ans
        return f(n, diff)


# Test Cases

test = Solution()
assert test.findTargetSumWays([1,1,1,1,1], 3) == 5
assert test.findTargetSumWays([1], 1) == 1
assert test.findTargetSumWays([1,1,1,1,1], 5) == 1

print("All passed")
        
