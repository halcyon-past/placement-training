"""
409. Longest Palindrome
Solved
Easy
Topics
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charFrequency = Counter(s)
        oddFrequencyCount = 0
        for frequency in charFrequency.values():
            if frequency % 2 == 1:
                oddFrequencyCount += 1
        if oddFrequencyCount > 1:
            return len(s) - oddFrequencyCount + 1
        return len(s)

# Test Cases
test = Solution()
assert test.longestPalindrome("abccccdd") == 7
assert test.longestPalindrome("a") == 1

print("All tests passed")