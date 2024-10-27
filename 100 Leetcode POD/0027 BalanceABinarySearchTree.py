"""
1382. Balance a Binary Search Tree
Solved
Medium
Topics
Companies
Hint
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""

from typing import List
import unittest

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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedArr = []
        self.inorderTraverse(root)
        return self.sortedArrayToBST(0, len(self.sortedArr) - 1)

    def inorderTraverse(self, root: TreeNode) -> None:
        if not root:
            return
        self.inorderTraverse(root.left)
        self.sortedArr.append(root)
        self.inorderTraverse(root.right)

    def sortedArrayToBST(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end) // 2
        root = self.sortedArr[mid]
        root.left = self.sortedArrayToBST(start, mid - 1)
        root.right = self.sortedArrayToBST(mid + 1, end)
        return root

def is_balanced(root: TreeNode) -> bool:
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return check_height(root) != -1

class TestBalanceBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = TreeNode(1)
        balanced_root = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(balanced_root))
        self.assertEqual(balanced_root.val, 1)
        self.assertIsNone(balanced_root.left)
        self.assertIsNone(balanced_root.right)

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        balanced_root = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(balanced_root))

    def test_balanced_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        balanced_root = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(balanced_root))

    def test_left_skewed(self):
        root = TreeNode(4)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        balanced_root = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(balanced_root))

    def test_complex_unbalanced(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(7)
        root.left.left.left = TreeNode(1)
        root.right.right = TreeNode(20)
        root.right.right.right = TreeNode(25)
        balanced_root = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(balanced_root))

if __name__ == "__main__":
    unittest.main()