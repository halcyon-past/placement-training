"""
440. K-th Smallest in Lexicographical Order
Solved
Hard
Topics
Companies
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
"""

class Solution:
    def getReqNum(self, a:int, b:int, n:int) -> int:
        gap = 0
        while a <= n:
            gap += min(n + 1, b) - a
            a *= 10
            b *= 10
        return gap

    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        i = 1
        while i < k:
            req = self.getReqNum(num, num + 1, n)
            if i + req <= k:
                i += req
                num += 1
            else:
                i += 1
                num *= 10
        return num

# Test Cases

test = Solution()

assert test.findKthNumber(13,2)==10
assert test.findKthNumber(1,1)==1

print("All Test Cases Passed")