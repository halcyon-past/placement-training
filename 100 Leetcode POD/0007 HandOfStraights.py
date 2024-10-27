"""
846. Hand of Straights
Solved
Medium
Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
 

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

class Solution(object):
    def find_successors(self, hand, groupSize, i, n):
        next_val = hand[i] + 1
        hand[i] = -1
        count = 1
        i += 1
        while i < n and count < groupSize:
            if hand[i] == next_val:
                next_val = hand[i] + 1
                hand[i] = -1
                count += 1
            i += 1
        return count == groupSize

    def isNStraightHand(self, hand, groupSize):
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        for i in range(n):
            if hand[i] >= 0:
                if not self.find_successors(hand, groupSize, i, n):
                    return False
        return True
        
# Time Complexity: (O(n \log n))

# Test Cases

test = Solution()
assert test.isNStraightHand([1,2,3,6,2,3,4,7,8],3)==True
assert test.isNStraightHand([1,2,3,4,5],4)==False

print("All Test Cases Passed")