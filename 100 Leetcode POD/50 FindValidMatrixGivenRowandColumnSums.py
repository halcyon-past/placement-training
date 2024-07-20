"""
1605. Find Valid Matrix Given Row and Column Sums
Solved
Medium
Topics
Companies
Hint
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]
 

Constraints:

1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 108
sum(rowSum) == sum(colSum)
"""

from typing import List

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows: int = len(rowSum)
        cols: int = len(colSum)
        cur_row: int = 0
        cur_col: int = 0
        res: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        while cur_row < rows or cur_col < cols:
            if cur_row >= rows:
                res[rows - 1][cur_col] = colSum[cur_col]
                cur_col += 1
                continue
            elif cur_col >= cols:
                res[cur_row][cols - 1] = rowSum[cur_row]
                cur_row += 1
                continue

            value_to_put: int = min(rowSum[cur_row], colSum[cur_col])
            rowSum[cur_row] -= value_to_put
            colSum[cur_col] -= value_to_put
            res[cur_row][cur_col] = value_to_put

            if rowSum[cur_row] == 0:
                cur_row += 1
            if colSum[cur_col] == 0:
                cur_col += 1

        return res
    
# Test Cases

test = Solution()
assert test.restoreMatrix([3,8], [4,7]) == [[3,0],[1,7]]
assert test.restoreMatrix([5,7,10], [8,6,8]) == [[5,0,0],[3,4,0],[0,2,8]]

print("All test cases pass")
