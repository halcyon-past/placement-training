"""

Code


Testcase
Testcase
Test Result
1552. Magnetic Force Between Two Balls
Solved
Medium
Topics
Companies
Hint
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:

[img](https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg)

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length
"""

from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            last_position, balls = position[0], 1
            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    last_position = position[i]
                    balls += 1
            if balls >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

# Test Cases

test = Solution()
assert test.maxDistance([1,2,3,4,7], 3) == 3
assert test.maxDistance([5,4,3,2,1,1000000000], 2) == 999999999

print("All test cases pass")