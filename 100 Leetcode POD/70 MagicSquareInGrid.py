"""
840. Magic Squares In Grid
Solved
Medium
Topics
Companies
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""

from typing import List

class Solution:
    def checkMagic(self,matrix,r,c):
        values = set()
        for i in range(r,r+3):
            for j in range(c,c+3):
                if matrix[i][j] in values or not (1 <= matrix[i][j] <= 9):
                    return 0
                values.add(matrix[i][j])
        
        for i in range(r,r+3):
            if sum(matrix[i][c:c+3])!=15:
                return 0
        
        for i in range(c,c+3):
            if (matrix[r][i]+matrix[r+1][i]+matrix[r+2][i]!=15):
                return 0

        if (
            (matrix[r][c]+matrix[r+1][c+1]+matrix[r+2][c+2]!=15)or
            (matrix[r][c+2]+matrix[r+1][c+1]+matrix[r+2][c]!=15)
        ):
            return 0
        
        return 1

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])

        res = 0

        for i in range(ROWS-2):
            for j in range(COLS-2):
                res += self.checkMagic(grid,i,j)
        
        return res


# Test Cases

test = Solution()
assert test.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]) == 1
assert test.numMagicSquaresInside([[8]]) == 0
assert test.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2],[1,1,1,1]]) == 1

print("All test cases pass")