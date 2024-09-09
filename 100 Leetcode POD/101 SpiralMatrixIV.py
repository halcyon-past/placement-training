"""
2326. Spiral Matrix IV
Solved
Medium
Topics
Companies
Hint
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""

from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        topRow, bottomRow = 0, m - 1
        leftColumn, rightColumn = 0, n - 1
        
        while head:
            # Fill top row
            for col in range(leftColumn, rightColumn + 1):
                if not head:
                    break
                matrix[topRow][col] = head.val
                head = head.next
            topRow += 1
            
            # Fill right column
            for row in range(topRow, bottomRow + 1):
                if not head:
                    break
                matrix[row][rightColumn] = head.val
                head = head.next
            rightColumn -= 1
            
            # Fill bottom row
            for col in range(rightColumn, leftColumn - 1, -1):
                if not head:
                    break
                matrix[bottomRow][col] = head.val
                head = head.next
            bottomRow -= 1
            
            # Fill left column
            for row in range(bottomRow, topRow - 1, -1):
                if not head:
                    break
                matrix[row][leftColumn] = head.val
                head = head.next
            leftColumn += 1
        
        return matrix
