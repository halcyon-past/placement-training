"""
1574. Shortest Subarray to be Removed to Make Array Sorted
Solved
Medium
Topics
Companies
Hint
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109
"""

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        max_left_length = next((i for i in range(1, len(arr)) if arr[i] < arr[i - 1]), len(arr))
        if max_left_length == len(arr):
            return 0

        result = len(arr) - max_left_length
        left = max_left_length - 1
        for right in reversed(range(len(arr))):
            while 0 <= left and arr[right] < arr[left]:
                left -= 1
            result = min(result, right - left - 1)
            if arr[right] < arr[right - 1]:
                break
        return result

# Test Cases

test = Solution()
assert test.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]) == 3
assert test.findLengthOfShortestSubarray([5,4,3,2,1]) == 4
assert test.findLengthOfShortestSubarray([1,2,3]) == 0

print("All passed")