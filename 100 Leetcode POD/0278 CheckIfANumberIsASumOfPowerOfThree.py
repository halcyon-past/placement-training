"""
1780. Check if Number is a Sum of Powers of Three
Medium
Topics
Companies
Hint
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107

"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            q, r=divmod(n, 3)
            if r==2: return False
            n=q
        return True


test = Solution()

assert test.checkPowersOfThree(12) == True
assert test.checkPowersOfThree(91) == True
assert test.checkPowersOfThree(21) == False

print("All tests passed successfully.")