#Sliding Window Problems
#Given an array of integers of size ‘n’.
#Our aim is to calculate the maximum sum of ‘k’
#consecutive elements in the array.
#Input  : arr[] = {100, 200, 300, 400}
#         k = 2
#Output : 700
#Explanation: Maximum sum is 700 which is sum of 300 and 400.


def sliding_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(sliding_window(arr, k))