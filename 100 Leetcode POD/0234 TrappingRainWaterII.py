"""
407. Trapping Rain Water II
Solved
Hard
Topics
Companies
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""

from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])

        pq = []  # Min-heap
        vis = [[False] * m for _ in range(n)]

        # Add first and last column
        for i in range(n):
            vis[i][0] = True
            vis[i][m - 1] = True
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][m - 1], i, m - 1))

        # Add first and last row
        for i in range(m):
            vis[0][i] = True
            vis[n - 1][i] = True
            heapq.heappush(pq, (heightMap[0][i], 0, i))
            heapq.heappush(pq, (heightMap[n - 1][i], n - 1, i))

        ans = 0
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]

        while pq:
            h, r, c = heapq.heappop(pq)

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc]:
                    ans += max(0, h - heightMap[nr][nc])
                    heapq.heappush(pq, (max(h, heightMap[nr][nc]), nr, nc))
                    vis[nr][nc] = True

        return ans


# Test Cases

test = Solution()

assert test.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) == 4
assert test.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]) == 10

print("All passed")