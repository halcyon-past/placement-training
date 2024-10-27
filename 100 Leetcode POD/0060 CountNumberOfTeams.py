"""
1395. Count Number of Teams
Solved
Medium
Topics
Companies
Hint
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
"""

from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            leftLess = leftGreater = rightLess = rightGreater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    rightLess += 1
                elif rating[k] > rating[j]:
                    rightGreater += 1
            
            count += leftLess * rightGreater + leftGreater * rightLess
        
        return count
    
# Test Cases

test = Solution()
assert test.numTeams([2,5,3,4,1])==3
assert test.numTeams([2,1,3])==0
assert test.numTeams([1,2,3,4])==4

print("All Test Cases Passed")