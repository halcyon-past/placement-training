"""
1248. Count Number of Nice Subarrays
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)
        cnt[0] = 1
        ans = 0
        t = 0
        for v in nums:
            t += v & 1
            if t - k >= 0:
                ans += cnt[t - k]
            cnt[t] += 1
        return ans
    
# Test Cases

test = Solution()
assert test.numberOfSubarrays([1,1,2,1,1], 3) == 2
assert test.numberOfSubarrays([2,4,6], 1) == 0
assert test.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16

print("All passed")