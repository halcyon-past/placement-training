"""
228. Summary Ranges
Solved
Easy
Topics
Companies
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        start = nums[0]
        end = nums[0]
        res =[]
        for i in range(1,len(nums),1):
            if nums[i] != nums[i-1] +1:
                if start == end:
                    res.append(f'{start}')
                else:
                    res.append(f'{start}->{end}')
                start=nums[i]
                end=nums[i]
            else:
                end = nums[i]
                
        if start!=end and f'{start}->{end}' not in res:
            res.append(f'{start}->{end}')
        elif f'{end}' not in res:
            res.append(f'{start}')
        return res

# Test Cases

test = Solution()
assert test.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
assert test.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]

print("All tests passed")