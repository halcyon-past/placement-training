# Merge Sort
"""
912. Sort an Array
Solved
Medium
Topics
Companies
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr)>1:
                mid = len(arr)//2
                left_half=arr[:mid]
                right_half=arr[mid:]
                merge_sort(left_half)
                merge_sort(right_half)

                i=j=k=0
                while i<len(left_half) and j<len(right_half):
                    if left_half[i]<right_half[j]:
                        arr[k]=left_half[i]
                        i += 1
                    else:
                        arr[k]=right_half[j]
                        j += 1
                    k+=1
                while i<len(left_half):
                    arr[k]=left_half[i]
                    i += 1
                    k += 1
                
                while j<len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1
            
        merge_sort(nums)
        return nums

# Test Cases

test = Solution()
assert test.sortArray([5,2,3,1]) == [1,2,3,5]
assert test.sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5]
assert test.sortArray([5,1,1,2,0,0,0]) == [0,0,0,1,1,2,5]

# Time Complexity: O(nlogn)
print("All Test Cases Passed")