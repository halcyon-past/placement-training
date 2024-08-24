"""
564. Find the Closest Palindrome
Solved
Hard
Topics
Companies
Hint
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
"""

class Solution:
    def nearestPalindromic(self, numberStr: str) -> str:
        number = int(numberStr)
        if number <= 10:
            return str(number - 1)
        if number == 11:
            return "9"

        length = len(numberStr)
        leftHalf = int(numberStr[:(length + 1) // 2])
        
        palindromeCandidates = [
            self.generatePalindromeFromLeft(leftHalf - 1, length % 2 == 0),
            self.generatePalindromeFromLeft(leftHalf, length % 2 == 0),
            self.generatePalindromeFromLeft(leftHalf + 1, length % 2 == 0),
            10**(length - 1) - 1,
            10**length + 1
        ]

        nearestPalindrome = 0
        minDifference = float('inf')

        for candidate in palindromeCandidates:
            if candidate == number:
                continue
            difference = abs(candidate - number)
            if difference < minDifference or (difference == minDifference and candidate < nearestPalindrome):
                minDifference = difference
                nearestPalindrome = candidate

        return str(nearestPalindrome)

    def generatePalindromeFromLeft(self, leftHalf: int, isEvenLength: bool) -> int:
        palindrome = leftHalf
        if not isEvenLength:
            leftHalf //= 10
        while leftHalf > 0:
            palindrome = palindrome * 10 + leftHalf % 10
            leftHalf //= 10
        return palindrome


# Test cases

test = Solution()

assert test.nearestPalindromic("123") == "121"
assert test.nearestPalindromic("1") == "0"
assert test.nearestPalindromic("10") == "9"

print("All tests passed")