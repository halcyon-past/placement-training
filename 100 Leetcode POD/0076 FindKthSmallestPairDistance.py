"""
719. Find K-th Smallest Pair Distance
Solved
Hard
Topics
Companies
Hint
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""

from typing import List

class Solution:
    def smallestDistancePair(self, numbers: List[int], k: int) -> int:
        numbers.sort()
        minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            if self.countPairsWithinDistance(numbers, midDistance) < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance
        
        return minDistance

    def countPairsWithinDistance(self, numbers: List[int], targetDistance: int) -> int:
        count = left = 0
        for right in range(1, len(numbers)):
            while numbers[right] - numbers[left] > targetDistance:
                left += 1
            count += right - left
        return count