"""
945. Minimum Increment to Make Array Unique
Solved
Medium
Topics
Companies
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament
    
# Time complexity: O(nlogn)

# Test Cases

test = Solution()
assert test.minIncrementForUnique([1,2,2]) == 1
assert test.minIncrementForUnique([3,2,1,2,1,7]) == 6
assert test.minIncrementForUnique([1,2,3,4,5]) == 0

print("All tests passed")