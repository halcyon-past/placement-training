"""
1460. Make Two Arrays Equal by Reversing Subarrays
Solved
Easy
Topics
Companies
Hint
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.
 

Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
"""

from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        elementCounts = [0] * 1001
        uniqueCount = 0
        
        for t, c in zip(target, arr):
            if elementCounts[t] == 0:
                uniqueCount += 1
            elementCounts[t] += 1
            
            if elementCounts[c] == 1:
                uniqueCount -= 1
            elementCounts[c] -= 1
        
        return uniqueCount == 0
    

# Test Cases

test = Solution()

assert test.canBeEqual([1,2,3,4], [2,4,1,3]) == True
assert test.canBeEqual([7], [7]) == True
assert test.canBeEqual([3,7,9], [3,7,11]) == False

print("All tests passed!")