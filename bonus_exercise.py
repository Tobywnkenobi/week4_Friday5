def max_sliding_window(nums, k):
    max_values = []
 
    for i in range(len(nums) - k + 1):
        print('window=', nums[i:i+k])
        max_values.append(max(nums[i:i+k]))
    return max_values

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
#print('i=',i)
#print('window=', nums[i:i+k])
#print('max_num=', max(nums[i:i+k]))
#print(len(nums) - k + 1)