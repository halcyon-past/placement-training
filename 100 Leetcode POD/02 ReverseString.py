"""
344. Reverse String
Solved
Easy
Topics
Companies
Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[~i]=s[~i],s[i]
        return s

# Time Complexity: O(N)
# Space Complexity: O(1)

#Test Cases

test = Solution()
assert test.reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert test.reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]
assert test.reverseString(["a","b","c","d"]) == ["d","c","b","a"]
assert test.reverseString(["a","b","c"]) == ["c","b","a"]

print("All tests passed")
