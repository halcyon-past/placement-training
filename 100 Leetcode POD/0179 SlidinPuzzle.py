"""
773. Sliding Puzzle
Solved
Hard
Topics
Companies
Hint
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
 

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
"""

from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }

        queue = deque([start])
        visited = set()
        visited.add(start)
        moves = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return moves

                index = curr.index('0')
                for neighbor in neighbors[index]:
                    ch = list(curr)
                    ch[index], ch[neighbor] = ch[neighbor], ch[index]
                    next_state = ''.join(ch)

                    if next_state not in visited:
                        queue.append(next_state)
                        visited.add(next_state)
            moves += 1

        return -1


# Test Cases

test = Solution()
assert test.slidingPuzzle([[1,2,3],[4,0,5]]) == 1
assert test.slidingPuzzle([[1,2,3],[5,4,0]]) == -1
assert test.slidingPuzzle([[4,1,2],[5,0,3]]) == 5

print("All passed")