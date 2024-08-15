"""
9. Palindrome Number
Solved
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x) -> bool:
        s = str(int(x))
        l=0
        r=len(s)-1
        while(l<r):
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        
# Test Cases

test = Solution()

assert test.isPalindrome(121) == True
assert test.isPalindrome(-121) == False
assert test.isPalindrome(10) == False
assert test.isPalindrome(-101) == False
assert test.isPalindrome(0) == True
assert test.isPalindrome(123) == False
assert test.isPalindrome(12321) == True

print("All passed")