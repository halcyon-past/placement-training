"""
1358. Number of Substrings Containing All Three Characters
Solved
Medium
Topics
Companies
Hint
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, cnt, letter, l=len(s), 0, 0, 0
        freq=[0]*3
        for r, c in enumerate(s):
            freq[ord(c)-97]+=1
            if freq[ord(c)-97]==1: letter+=1
            while letter==3:
                freq[ord(s[l])-97]-=1
                if freq[ord(s[l])-97]==0: letter-=1
                l+=1
            cnt+=l
        return cnt