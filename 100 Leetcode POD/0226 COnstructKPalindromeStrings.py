"""
1400. Construct K Palindrome Strings
Solved
Medium
Topics
Companies
Hint
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105
"""

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        char_count = Counter(s)
        odd_count = sum(freq % 2 for freq in char_count.values())
        return odd_count <= k


# Test Cases

test = Solution()

assert test.canConstruct("annabelle", 2) == True
assert test.canConstruct("leetcode", 3) == False
assert test.canConstruct("true", 4) == True

print("All tests passed")