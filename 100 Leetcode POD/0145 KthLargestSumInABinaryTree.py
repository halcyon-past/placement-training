"""
2583. Kth Largest Sum in a Binary Tree
Solved
Medium
Topics
Companies
Hint
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

Checkout my Solution at: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/solutions/5951204/bfs-sort-solution-beats-99-22-python
"""

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class to calculate kth largest level sum
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        q = deque([root])

        # BFS to calculate level sums
        while q:
            n = len(q)
            level_sum = 0

            # Process all nodes at the current level
            for _ in range(n):
                node = q.popleft()
                level_sum += node.val

                # Add child nodes to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level_sum)
        
        # If k is greater than the number of levels, return -1
        if k > len(res):
            return -1
        
        # Sort the sums in descending order and return the k-th largest
        res.sort(reverse=True)
        return res[k-1]

# Function to build a binary tree from the list (input array)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current_node = queue.popleft()

        if values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1

    return root

# Main function to run the solution with the provided input
if __name__ == "__main__":
    # Example input 1: [5,8,9,2,1,3,7,4,6], k = 2
    values = [5, 8, 9, 2, 1, 3, 7, 4, 6]
    k = 2

    # Example input 2: [1,2,None,3], k = 1
    # values = [1, 2, None, 3]
    # k = 1

    # Build the binary tree from the input array
    root = build_tree(values)

    # Create an instance of the Solution class
    solution = Solution()

    # Get the kth largest level sum
    result = solution.kthLargestLevelSum(root, k)

    # Print the result
    print(f"The {k}-th largest level sum is: {result}")
