"""
61. Rotate List
Solved
Medium
Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def length(self, node: Optional[ListNode]) -> int:
        n = 0
        while node:
            node = node.next
            n += 1
        return n

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        n=self.length(head)
        if k%n==0:
            return head
        
        k=k%n

        node=head
        for _ in range(n-k-1):
            node = node.next
        
        res = node.next
        node.next = None

        tail = res
        while tail.next:
            tail = tail.next
        
        tail.next=head
        return res

        