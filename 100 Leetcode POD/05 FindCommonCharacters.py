"""
1002. Find Common Characters
Solved
Easy
Topics
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

class Solution:
    def count(self,word):
        freq = [0]*26
        for char in word:
            freq[ord(char)-ord('a')] += 1
        return freq
    
    def intersection(self,freq1,freq2):
        return [min(f1,f2) for f1,f2 in zip(freq1,freq2)]

    def commonChars(self, words: list[str]) -> list[str]:
        last = self.count(words[0])
        for word in words[1:]:
            last = self.intersection(last,self.count(word))
        
        result = []
        for i in range(26):
            result.extend([chr(i+ord('a'))]*last[i])
        
        return result
    
# Time Complexity: O(N*M)
# Space Complexity: O(M)

# Test Cases

test = Solution()
assert test.commonChars(["bella","label","roller"]) == ["e","l","l"]
assert test.commonChars(["cool","lock","cook"]) == ["c","o"]

print("All tests passed")