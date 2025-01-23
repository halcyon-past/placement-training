"""
1267. Count Servers that Communicate
Solved
Medium
Topics
Companies
Hint
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        Rows = [sum(row) for row in grid]
        Col = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        return sum(1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1 and (Rows[i] > 1 or Col[j] > 1))


# Test Case

test = Solution()

assert test.countServers([[1,0],[0,1]]) == 0
assert test.countServers([[1,0],[1,1]]) == 3
assert test.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4

print("All tests passed")