"""
916. Word Subsets
Solved
Medium
Topics
Companies
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""

from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxCharFreq = [0] * 26
        tempCharFreq = [0] * 26

        for word in words2:
            for ch in word:
                tempCharFreq[ord(ch) - ord('a')] += 1
            for i in range(26):
                maxCharFreq[i] = max(maxCharFreq[i], tempCharFreq[i])
            tempCharFreq = [0] * 26

        universalWords = []

        for word in words1:
            for ch in word:
                tempCharFreq[ord(ch) - ord('a')] += 1
            isUniversal = True
            for i in range(26):
                if maxCharFreq[i] > tempCharFreq[i]:
                    isUniversal = False
                    break
            if isUniversal:
                universalWords.append(word)
            tempCharFreq = [0] * 26

        return universalWords
    
# Test cases

test = Solution()

assert test.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]) == ["facebook","google","leetcode"]
assert test.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]) == ["apple","google","leetcode"]

print("All tests passed")