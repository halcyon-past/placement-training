"""
3133. Minimum Array End
Solved
Medium
Topics
Companies
Hint
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

 

Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

 

Constraints:

1 <= n, x <= 108
"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n_1, ans, j=n-1, 0, 0
        for i in range(56):
            if (x>>i)&1: 
                ans|=(1<<i)
            else:
                if (n_1>>j)&1: ans|=(1<<i)
                j+=1
        return ans

# Test Cases

test = Solution()
assert test.minEnd(3, 4) == 6
assert test.minEnd(2, 7) == 15

print("All tests passed")