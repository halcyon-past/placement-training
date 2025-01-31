"""
827. Making A Large Island
Solved
Hard
Topics
Companies
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""

from typing import List

class Solution(object):
    def largestIsland(self, grid: List[List[int]])->int:
        n = len(grid)
        directions = [ (1,0), (-1,0), (0,1), (0,-1) ]
        key = []
        current_id = 2

        def dfs(i, j, id):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = id
            count = 1
            for dx, dy in directions:
                count += dfs(i + dx, j + dy, id)
            return count

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, current_id)
                    key.append(size)
                    current_id += 1

        if not key:
            return 1

        max_size = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    current = 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != 0:
                            island_id = grid[ni][nj]
                            if island_id not in seen:
                                current += key[island_id - 2]
                                seen.add(island_id)
                    max_size = max(max_size, current)

        return max_size if max_size != 0 else n * n


# Test Cases

test = Solution()
assert test.largestIsland([[1,0],[0,1]]) == 3
assert test.largestIsland([[1,1],[1,0]]) == 4
assert test.largestIsland([[1,1],[1,1]]) == 4

print("All passed")