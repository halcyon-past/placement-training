"""
539. Minimum Time Difference
Solved
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        minutes.sort()
        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])
        min_diff = min(min_diff, 24 * 60 - minutes[-1] + minutes[0])     
        return min_diff

# Test Cases

test = Solution()
assert test.findMinDifference(["23:59","00:00"]) == 1
assert test.findMinDifference(["00:00","23:59","00:00"]) == 0
assert test.findMinDifference(["00:00","23:59","00:01"]) == 1

print("All tests passed")