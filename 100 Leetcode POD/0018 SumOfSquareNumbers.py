"""
633. Sum of Square Numbers
Solved
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
"""

from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)
            if b == int(b):
                return True
        return False
        
# Time Complexity: O(sqrt(c))

# Test Cases

assert Solution().judgeSquareSum(5) == True
assert Solution().judgeSquareSum(3) == False
assert Solution().judgeSquareSum(4) == True
assert Solution().judgeSquareSum(25) == True
assert Solution().judgeSquareSum(7) == False

print("All test cases passed")