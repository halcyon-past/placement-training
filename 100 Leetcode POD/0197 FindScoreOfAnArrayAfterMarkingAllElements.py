"""
2593. Find Score of an Array After Marking All Elements
Solved
Medium
Topics
Companies
Hint
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

 

Example 1:

Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
Example 2:

Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
"""

from typing import List
from collections import deque

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        q = deque()

        # Traverse through the array
        for i in range(n):
            # If queue is not empty and the current number is greater than or equal to the last in queue
            if q and nums[i] >= q[-1]:
                skip = False
                # Process the elements in the queue
                while q:
                    add = q.pop()
                    if not skip:
                        score += add
                    skip = not skip
                continue

            # Add current element to the queue
            q.append(nums[i])

        # Final processing of remaining elements in the queue
        skip = False
        while q:
            add = q.pop()
            if not skip:
                score += add
            skip = not skip

        return score


# Test Cases

test = Solution()

assert test.findScore([2,1,3,4,5,2]) == 7
assert test.findScore([2,3,5,1,3,2]) == 5
assert test.findScore([1,2,3,4,5,6]) == 9

print("All test cases pass")