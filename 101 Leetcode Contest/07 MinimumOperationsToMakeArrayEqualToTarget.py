"""
100329. Minimum Operations to Make Array Equal to Target
Solved
Hard
You are given two positive integer arrays nums and target, of the same length.

In a single operation, you can select any 
subarray
 of nums and increment or decrement each element within that subarray by 1.

Return the minimum number of operations required to make nums equal to the array target.

 

Example 1:

Input: nums = [3,5,1,2], target = [4,6,2,4]

Output: 2

Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..3] by 1, nums = [4,6,2,3].
- Increment nums[3..3] by 1, nums = [4,6,2,4].

Example 2:

Input: nums = [1,3,2], target = [2,1,4]

Output: 5

Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..0] by 1, nums = [2,3,2].
- Decrement nums[1..1] by 1, nums = [2,2,2].
- Decrement nums[1..1] by 1, nums = [2,1,2].
- Increment nums[2..2] by 1, nums = [2,1,3].
- Increment nums[2..2] by 1, nums = [2,1,4].

 

Constraints:

1 <= nums.length == target.length <= 105
1 <= nums[i], target[i] <= 108
"""

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        if len(nums) != len(target):
            return -1

        diff = [nums[i] - target[i] for i in range(len(nums))]
        
        operations = 0
        for i in range(len(diff)):
            if i == 0 or diff[i] * diff[i-1] <= 0:
                operations += abs(diff[i])
            else:
                operations += max(abs(diff[i]) - abs(diff[i-1]), 0)
                
        return operations
    
# Test Cases

test = Solution()
assert test.minimumOperations([3,5,1,2], [4,6,2,4]) == 2
assert test.minimumOperations([1,3,2], [2,1,4]) == 5

print("All test cases pass")