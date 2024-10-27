"""
1277. Count Square Submatrices with All Ones
Solved
Medium
Topics
Companies
Hint
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = sum(matrix[0])
        for i in range(1, n):
            ans += matrix[i][0]
            for j in range(1, m):
                if matrix[i][j]:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    ans += matrix[i][j]
        return ans    


# Test Cases

test = Solution()
assert test.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]) == 15
assert test.countSquares([[1,0,1],[1,1,0],[1,1,0]]) == 7

print("All passed")