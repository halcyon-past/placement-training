"""
1791. Find Center of Star Graph
Solved
Easy
Topics
Companies
Hint
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
 

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
"""

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

def test_find_center():
    solution = Solution()
    
    # Test case 1
    edges1 = [[1, 2], [2, 3], [4, 2]]
    assert solution.findCenter(edges1) == 2, f"Test case 1 failed. Expected 2, got {solution.findCenter(edges1)}"
    
    # Test case 2
    edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
    assert solution.findCenter(edges2) == 1, f"Test case 2 failed. Expected 1, got {solution.findCenter(edges2)}"
    
    # Test case 3
    edges3 = [[3, 4], [2, 3], [3, 1]]
    assert solution.findCenter(edges3) == 3, f"Test case 3 failed. Expected 3, got {solution.findCenter(edges3)}"
    
    # Test case 4
    edges4 = [[5, 6], [6, 7], [6, 8], [9, 6]]
    assert solution.findCenter(edges4) == 6, f"Test case 4 failed. Expected 6, got {solution.findCenter(edges4)}"
    
    # Test case 5
    edges5 = [[10, 20], [20, 30], [40, 20]]
    assert solution.findCenter(edges5) == 20, f"Test case 5 failed. Expected 20, got {solution.findCenter(edges5)}"
    
    print("All test cases passed!")

# Run the tests
test_find_center()
