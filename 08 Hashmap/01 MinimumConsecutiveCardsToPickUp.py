"""
2260. Minimum Consecutive Cards to Pick Up
Solved
Medium
Topics
Companies
Hint
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

1 <= cards.length <= 105
0 <= cards[i] <= 106
"""

from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        uni=set(cards)
        if(len(uni)==len(cards)):
            return -1
        d={}
        mini=len(cards)
        for i in range(0,len(cards)):
            if cards[i] in d:
                mini=min(mini,i-d[cards[i]]+1)
                d[cards[i]]=i
            else:
                d[cards[i]]=i
        return mini

# Test Cases

test = Solution()
assert test.minimumCardPickup([3,4,2,3,4,7]) == 4
assert test.minimumCardPickup([1,0,5,3]) == -1

print("All tests passed")