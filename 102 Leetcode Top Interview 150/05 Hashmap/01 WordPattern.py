"""
290. Word Pattern
Solved
Easy
Topics
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        if len(pattern)!=len(s.split()):
            return False
        for i,j in zip(pattern,s.split()):
            if i in d:
                if d[i]!=j:
                    return False
            d[i]=j
        if len(set(d.values()))!=len(d.values()):
            return False
        return True

# Test Cases

test = Solution()
assert test.wordPattern("abba", "dog cat cat dog") == True
assert test.wordPattern("abba", "dog cat cat fish") == False
assert test.wordPattern("aaaa", "dog cat cat dog") == False
assert test.wordPattern("aaa", "dog dog dog dog") == False


print("All test cases pass")