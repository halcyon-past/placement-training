"""
1718. Construct the Lexicographically Largest Valid Sequence
Solved
Medium
Topics
Companies
Hint
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
"""

from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        az=n*2-1
        ans=[0]*az
        def dfs(pos, viz=0):
            if pos==az:
                return viz.bit_count()==n
            if ans[pos]!=0:
                return dfs(pos+1, viz)
            for j in range(n, 0, -1):
                if (viz>>j)&1==1: 
                    continue
                next_pos=pos+j if j>1 else pos

                if next_pos>=az or ans[next_pos]!=0:
                    continue
                ans[pos]=ans[next_pos]=j
                viz|=(1<<j)

                if dfs(pos+1, viz):
                    return True
                ans[pos]=ans[next_pos]=0
                viz&=(~(1<<j))
            return False

        dfs(0)
        return ans  
    
# Test Cases

test = Solution()

assert test.constructDistancedSequence(3) == [3,1,2,3,2]
assert test.constructDistancedSequence(5) == [5,3,1,4,3,5,2,4,2]

print("All tests passed!")