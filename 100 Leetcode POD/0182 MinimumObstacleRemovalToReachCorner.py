"""
2290. Minimum Obstacle Removal to Reach Corner
Solved
Hard
Topics
Companies
Hint
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

Example 1:


Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:


Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""

from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        deque_ = deque([(0, 0, 0)]) 
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        while deque_:
            x, y, obstacles_removed = deque_.popleft()
            if x == m - 1 and y == n - 1:
                return obstacles_removed
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        deque_.appendleft((nx, ny, obstacles_removed))
                    else:
                        deque_.append((nx, ny, obstacles_removed + 1))
        return -1


# Test Cases

test = Solution()
assert test.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]) == 2
assert test.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]) == 0
assert test.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]) == 2

print("All passed")