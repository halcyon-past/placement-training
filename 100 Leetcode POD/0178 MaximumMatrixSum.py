"""
1975. Maximum Matrix Sum
Solved
Medium
Topics
Companies
Hint
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
"""

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_value = float('inf')
        total_sum = 0
        neg_count = 0

        for row in matrix:
            for value in row:
                if value < 0:
                    neg_count += 1
                abs_value = abs(value)
                min_value = min(min_value, abs_value)
                total_sum += abs_value

        if neg_count % 2 == 0:
            return total_sum
        return total_sum - 2 * min_value

# Test Cases

test = Solution()
assert test.maxMatrixSum([[1,-1],[-1,1]]) == 4
assert test.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]) == 16

print("All passed")