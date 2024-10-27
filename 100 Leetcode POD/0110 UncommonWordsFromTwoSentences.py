"""
884. Uncommon Words from Two Sentences
Solved
Easy
Topics
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""

from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_s1 = s1.split()
        words_s2 = s2.split()
        all_words = words_s1 + words_s2
        word_count = Counter(all_words)
        return [word for word in word_count if word_count[word] == 1]


# Test Cases

test = Solution()
assert test.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet","sour"]
assert test.uncommonFromSentences("apple apple", "banana") == ["banana"]
assert test.uncommonFromSentences("apple apple", "banana banana") == []

print("All passed")