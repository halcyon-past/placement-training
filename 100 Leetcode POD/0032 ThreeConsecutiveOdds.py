"""
1550. Three Consecutive Odds
Solved
Easy
Topics
Companies
Hint
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        len=0
        for i in arr:
            if (i&1):
                len+=1
            else:
                len=0
            if(len==3):
                return True
        return False
    
# Test cases

test = Solution()
assert test.threeConsecutiveOdds([2,6,4,1]) == False
assert test.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]) == True
print("All tests passed")