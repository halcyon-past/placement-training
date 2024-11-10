"""
3097. Shortest Subarray With OR at Least K II
Medium
Topics
Companies
Hint
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty 
subarray
 of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
"""

from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bitCount = [0] * 32
        currentOR = 0
        left = 0
        minLength = float('inf')
        
        for right in range(n):
            currentOR |= nums[right]
            
            for bit in range(32):
                if nums[right] & (1 << bit):
                    bitCount[bit] += 1
            
            while left <= right and currentOR >= k:
                minLength = min(minLength, right - left + 1)
                
                updatedOR = 0
                for bit in range(32):
                    if nums[left] & (1 << bit):
                        bitCount[bit] -= 1
                    if bitCount[bit] > 0:
                        updatedOR |= (1 << bit)
                
                currentOR = updatedOR
                left += 1
        
        return minLength if minLength != float('inf') else -1


# Test Cases

test = Solution()
assert test.minimumSubarrayLength([1,2,3], 2) == 1
assert test.minimumSubarrayLength([2,1,8], 10) == 3
assert test.minimumSubarrayLength([1,2], 0) == 1

print("All tests passed")