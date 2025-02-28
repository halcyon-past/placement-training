"""
1092. Shortest Common Supersequence 
Solved
Hard
Topics
Companies
Hint
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""

from concurrent.futures import ThreadPoolExecutor

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.generateLCS, str1, str2)
            return future.result()

    def generateLCS(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        lcsMatrix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    lcsMatrix[i][j] = lcsMatrix[i - 1][j - 1] + 1
                else:
                    lcsMatrix[i][j] = max(lcsMatrix[i - 1][j], lcsMatrix[i][j - 1])

        row, col = m, n
        result = []

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                result.append(str1[row - 1])
                row, col = row - 1, col - 1
            elif lcsMatrix[row - 1][col] > lcsMatrix[row][col - 1]:
                result.append(str1[row - 1])
                row -= 1
            else:
                result.append(str2[col - 1])
                col -= 1

        while row > 0:
            result.append(str1[row - 1])
            row -= 1
        while col > 0:
            result.append(str2[col - 1])
            col -= 1

        return "".join(result[::-1])