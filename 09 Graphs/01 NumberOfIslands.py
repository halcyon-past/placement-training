"""
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows , cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if (
                        r in range(rows) and
                        c in range(cols) and
                        (r,c) not in visit and
                        grid[r][c] == "1"
                        ):
                        q.append((r,c))
                        visit.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        
        return island


# Test Cases

test = Solution()

assert test.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]) == 1

assert test.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]) == 3

assert test.numIslands([
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"]
    ]) == 1


print("All passed")