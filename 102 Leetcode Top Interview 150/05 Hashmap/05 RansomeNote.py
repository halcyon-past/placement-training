"""
383. Ransom Note
Solved
Easy
Topics
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = defaultdict(int)
        for char in magazine:
            dictionary[char] += 1
        for char in ransomNote:
            if dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        
        return True

# Test Cases

test = Solution()
assert test.canConstruct("a", "b") == False
assert test.canConstruct("aa", "ab") == False
assert test.canConstruct("aa", "aab") == True

print("All tests passed")