"""
2054. Two Best Non-Overlapping Events
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106
"""

from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        max_until = []
        max_value = 0
        for _, end, value in events:
            max_value = max(max_value, value)
            max_until.append((end, max_value))
        result = 0
        for start, end, value in events:
            result = max(result, value)
            idx = bisect.bisect_left(max_until, (start, 0)) - 1
            if idx >= 0:
                result = max(result, value + max_until[idx][1])
        
        return result

# Test case

test = Solution()
assert test.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]) == 4
assert test.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]) == 5
assert test.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]) == 8

print("All test cases pass")