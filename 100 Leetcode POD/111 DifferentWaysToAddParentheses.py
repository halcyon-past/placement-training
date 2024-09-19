"""
241. Different Ways to Add Parentheses
Solved
Medium
Topics
Companies
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
"""

from typing import List

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        return (f:=lambda s:[eval(f'{l}{c}{r}') for i,c in enumerate(s) if c<'0' for l in f(s[:i]) for r in f(s[i+1:])] or [int(s)])(s)


# Test Cases

test = Solution()
assert test.diffWaysToCompute("2-1-1") == [0, 2]
assert test.diffWaysToCompute("2*3-4*5") == [-34,-14,-10,-10,10]

print("All passed")