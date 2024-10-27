"""
974. Subarray Sums Divisible by K
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
"""

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:  
                mod += k
            if mod in prefix_map:
                count += prefix_map[mod]
                prefix_map[mod] += 1
            else:
                prefix_map[mod] = 1
        
        return count
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# Test Cases

test = Solution()
assert test.subarraysDivByK([4,5,0,-2,-3,1], 5) == 7
assert test.subarraysDivByK([5], 9) == 0

print("All tests passed")