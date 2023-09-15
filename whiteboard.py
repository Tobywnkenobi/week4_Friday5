"""
# Sliding Window Maximum Whiteboard Exercise

# Problem Description:

# You are given an array of integers nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Your task is to return an array that contains the maximum number for each window as it moves from left to right across nums.

# Inputs:
# An array of integers, nums.
# An integer k representing the size of the sliding window.

# Outputs:
# An array of integers representing the maximum element in each of the sliding windows.

# Example:

# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]

# Constraints:
# The array nums will have at least k elements.
# Time complexity should ideally be better than O(n*k).

"""
def sliding_window(nums, k):
    if not nums:
        return []
    
    n = len(nums)
    if n * k == 0:
        return []
    
    output = []
    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n-1]

    for i in range(1, n):
        if i % k == 0:
            left[i] = nums [i]
        else:
            left[i] = max(left[i - 1], nums[i])

    for i in range(n -2, -1, -1):
        if (i + 1) % k == 0:
            right[i] = nums[i]
        else:
            right[i] = max(right[i + 1], nums[i])

    for i in range(n - k +1):
        output.append(max(right[i], left[i + k -1]))

    return output

nums = [9, 7, 2, 4, 6, 8, 2, 1, 5]
k = 4

sliding_window(nums, k)
result = sliding_window(nums,k)

print("Input:", nums)
print("window size:", k)
print("output:", result)


