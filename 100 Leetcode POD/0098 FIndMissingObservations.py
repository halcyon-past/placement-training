"""
2028. Find Missing Observations
Solved
Medium
Topics
Companies
Hint
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
 

Constraints:

m == rolls.length
1 <= n, m <= 105
1 <= rolls[i], mean <= 6
"""

from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total=(n+m)*mean
        miss = total-sum(rolls)
        if miss>6*n or miss<n: return []
        q,r=divmod(miss,n)
        return [q+1]*r+[q]*(n-r)

# Test Cases

test = Solution()

assert test.missingRolls([3,2,4,3], 4, 2) == [6,6]
assert test.missingRolls([1,5,6], 3, 4) == [2,3,2,2]
assert test.missingRolls([1,2,3,4], 6, 4) == []

print("All passed")