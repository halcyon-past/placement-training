"""
2181. Merge Nodes in Between Zeros
Solved
Medium
Topics
Companies
Hint
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

 

Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
Example 2:


Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
 

Constraints:

The number of nodes in the list is in the range [3, 2 * 105].
0 <= Node.val <= 1000
There are no two consecutive nodes with Node.val == 0.
The beginning and end of the linked list have Node.val == 0.
"""

from typing import Optional

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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        head = head.next
        sum_val = 0
        while head:
            if head.val == 0:
                cur.next = ListNode(sum_val)
                cur = cur.next
                sum_val = 0
            sum_val += head.val
            head = head.next
        return dummy.next

# Test cases

test = Solution()

# Test 1
node1 = ListNode(0)
node2 = ListNode(3)
node3 = ListNode(1)
node4 = ListNode(0)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(2)
node8 = ListNode(0)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = None

result = test.mergeNodes(node1)
assert result.val == 4
assert result.next.val == 11
assert result.next.next == None

# Test 2
node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(0)
node4 = ListNode(3)
node5 = ListNode(0)
node6 = ListNode(2)
node7 = ListNode(2)
node8 = ListNode(0)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = None

result = test.mergeNodes(node1)
assert result.val == 1
assert result.next.val == 3
assert result.next.next.val == 4
assert result.next.next.next == None

print("All tests passed")