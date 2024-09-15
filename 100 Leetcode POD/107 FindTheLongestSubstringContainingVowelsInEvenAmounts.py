"""
1371. Find the Longest Substring Containing Vowels in Even Counts
Solved
Medium
Topics
Companies
Hint
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapy = [-2] * 32
        mapy[0] = -1

        max_len = 0
        mask = 0

        for i, char in enumerate(s):
            if char == 'a':
                mask ^= 1
            elif char == 'e':
                mask ^= 2
            elif char == 'i':
                mask ^= 4
            elif char == 'o':
                mask ^= 8
            elif char == 'u':
                mask ^= 16

            prev = mapy[mask]
            if prev == -2:
                mapy[mask] = i
            else:
                max_len = max(max_len, i - prev)

        return max_len