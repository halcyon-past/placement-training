"""
1405. Longest Happy String
Solved
Medium
Topics
Companies
Hint
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""

from heapq import heappush, heappop
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxh = []
        if a:
            heappush(maxh, (-a, 'a'))
        if b:
            heappush(maxh, (-b, 'b'))
        if c:
            heappush(maxh, (-c, 'c'))

        res = ""
        while maxh:
            f1, c1 = heapq.heappop(maxh)
            f1 *= -1

            if len(res)>=2 and res[-1]==res[-2]==c1:
                if not maxh:
                    return res
                f2, c2 = heapq.heappop(maxh)
                f2 *= -1
                res += c2
                f2 -= 1
                if f2:
                    heapq.heappush(maxh,(-1*f2, c2))
                heapq.heappush(maxh,(-1*f1, c1))
                continue


            res += c1
            f1 -= 1
            if f1:
                heapq.heappush(maxh,(-1*f1, c1))

        return res