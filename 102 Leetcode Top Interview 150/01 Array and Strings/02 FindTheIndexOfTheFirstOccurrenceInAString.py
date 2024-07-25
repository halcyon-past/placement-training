# Knuth-Morris-Pratt KMP String Matching Algorithm

"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        lps=[0]*len(needle)
        prevLPS,i=0,1
        while i<len(needle):
            if needle[i]==needle[prevLPS]:
                lps[i] = prevLPS+1
                prevLPS += 1
                i += 1
            elif prevLPS==0:
                lps[i]=0
                i+=1
            else:
                prevLPS=lps[prevLPS-1]
            
        i=0
        j=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i,j=i+1,j+1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
            if j==len(needle):
                return i-len(needle)
        return -1

# Test Cases

test = Solution()
assert test.strStr("sadbutsad", "sad") == 0
assert test.strStr("leetcode", "leeto") == -1

print("All test cases pass")