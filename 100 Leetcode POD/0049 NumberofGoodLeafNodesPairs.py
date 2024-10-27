"""
1530. Number of Good Leaf Nodes Pairs
Solved
Medium
Topics
Companies
Hint
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

 

Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
 

Constraints:

The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10
"""

from typing import List, Dict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.map = {}
        self.leaves = []
        self.findLeaves(root, [], self.leaves, self.map)
        res = 0
        for i in range(len(self.leaves)):
            for j in range(i + 1, len(self.leaves)):
                list_i, list_j = self.map[self.leaves[i]], self.map[self.leaves[j]]
                for k in range(min(len(list_i), len(list_j))):
                    if list_i[k] != list_j[k]:
                        dist = len(list_i) - k + len(list_j) - k
                        if dist <= distance:
                            res += 1
                        break
        return res

    def findLeaves(self, node: TreeNode, trail: List[TreeNode], leaves: List[TreeNode], map: Dict[TreeNode, List[TreeNode]]):
        if not node:
            return
        tmp = trail[:]
        tmp.append(node)
        if not node.left and not node.right:
            map[node] = tmp
            leaves.append(node)
            return
        self.findLeaves(node.left, tmp, leaves, map)
        self.findLeaves(node.right, tmp, leaves, map)
        