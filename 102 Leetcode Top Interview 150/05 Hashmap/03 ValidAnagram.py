"""
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = Counter(s)
        y = Counter(t)
        return x==y

# Test Cases

test = Solution()
assert test.isAnagram("anagram", "nagaram") == True
assert test.isAnagram("rat", "car") == False


print("All Test Cases Passed")