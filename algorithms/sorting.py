# Sorting Algorithms 

test_cases = [[], [0], [0,0], [0,1], [1,0]]

# Is Sorted
# Time Complexity: O(n)
# Memory Usage:	   O(1)
# Params: List
# Return: True if list is sorted else false

def is_sorted(nums):
	for idx in range(len(nums)-1):
		if nums[idx] > nums[idx+1]: 
			return False
	return True

# Bubble Sort 
# Time Complexity
# Best Case:	O(n)
# Worst Case:  	O(n^2)
# Average Case: O(n*logn)
# Memory Usage: O(1)

def bubble_sort(nums):
	flag = False
	while not flag:
		flag = True
		for idx in range(len(nums)-1):
			num = nums[idx]
			if num > nums[idx+1]:
				nums[idx] = nums[idx+1]
				nums[idx+1] = num
				flag = False
	return nums

# Placement Sort 
# Time Complexity 
# Best Case:	O(n)
# Worst Case:	O(n^2)
# Average Case:	O(n*logn)
# Memory Usage: O(n)

def place_sort(nums):
	result = []
	for num in nums:
		i = 0
		while len(result) > i and result[i] <  num:
			i += 1
		result = result[:i] + [num] + result[i:]
	return result

