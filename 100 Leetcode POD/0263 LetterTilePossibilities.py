"""
1079. Letter Tile Possibilities
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = [0] * 26
        fac = [1] * (len(tiles) + 1)
        for i in range(1, len(tiles) + 1):
            fac[i] = i * fac[i - 1]
        for c in tiles:
            counts[ord(c) - ord('A')] += 1
        lengthcounts = [0] * (len(tiles) + 1)
        lengthcounts[0] = 1
        for i in range(26):
            if counts[i] > 0:
                temp = [0] * (len(tiles) + 1)
                for j in range(len(tiles) + 1):
                    if lengthcounts[j] > 0:
                        for k in range(1, counts[i] + 1):
                            totallength = j + k
                            temp[totallength] += lengthcounts[j] * fac[totallength] // (fac[k] * fac[j])
                for j in range(len(tiles) + 1):
                    lengthcounts[j] += temp[j]
        return sum(lengthcounts[1:])


# Test Cases

test = Solution()

assert test.numTilePossibilities("AAB") == 8
assert test.numTilePossibilities("AAABBC") == 188
assert test.numTilePossibilities("V") == 1

print("All passed")