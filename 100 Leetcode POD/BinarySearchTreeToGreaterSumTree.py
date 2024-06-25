"""
1038. Binary Search Tree to Greater Sum Tree
Solved
Medium
Topics
Companies
Hint
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
Output: [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
Example 2:

Input: root = [0,None,1]
Output: [1,None,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.
 

Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left = None
        self.right = right = None
        
    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"

class Solution:
    def __init__(self):
        self.sum = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.sum += root.val
            root.val = self.sum
            self.bstToGst(root.left) 
        return root

    def reset_sum(self):
        self.sum = 0

# Helper function to insert nodes in level order to create the tree from list
def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i]) if arr[i] is not None else None
        root = temp

        if root is not None:
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    
    return root

# Helper function to create a tree from a list
def createTree(lst):
    return insertLevelOrder(lst, None, 0, len(lst))

# Test function
def test_bstToGst():
    sol = Solution()

    # Example 1
    root1 = createTree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    expected1 = createTree([30,36,21,36,35,26,15,None,None,None,33,None,None,None,8])
    sol.reset_sum()
    assert sol.bstToGst(root1) == expected1, f"Expected {expected1}, but got {sol.bstToGst(root1)}"

    # Example 2
    root2 = createTree([0, None, 1])
    expected2 = createTree([1, None, 1])
    sol.reset_sum()
    assert sol.bstToGst(root2) == expected2, f"Expected {expected2}, but got {sol.bstToGst(root2)}"

    print("All test cases passed successfully!")

# Run the tests
test_bstToGst()
