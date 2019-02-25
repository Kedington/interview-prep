# Searching Algorithms

# Collection of Search Algorithms 

# Basic Search Algorithm 
# Best Case: 	O(1)
# Worst Case: 	O(n)
# Memory: 		O(1)
# Params: A list of unsorted integers and an element 
# Return: idx if one exists else None

def search(nums, elm):
	for idx in range(len(nums)):
		if nums[idx] == elm:
			return idx 

# Binary Search 
# Time:  O(logn)
# Space: O(1)
# Params: A list of sorted integers and an element
# Return True if elm in list else false

def binary_search(nums, elm):
	while nums:
		mid = int(len(nums)/2)
		if elm == nums[mid]:
			return True
		elif elm > nums[mid]:
			nums = nums[mid+1:]
		elif elm < nums[mid]:
			nums = nums[:mid]
	return False

# Binary Search idx
# Time:  O(logn)
# Space: O(1)
# Params: A list of sorted integers and an element
# Return idx if element exists else None

def binary_search_idx(nums, elm):
	idx = 0
	while nums:
		mid = int(len(nums)/2)
		if elm == nums[mid]:
			return idx + mid
		elif elm > nums[mid]:
			nums = nums[mid+1:]
			idx += mid + 1
		elif elm < nums[mid]:
			nums = nums[:mid]
	return None

# Nth Element
# Time:  O(n) 
# Space: O(n)
# Params: A list of unique unsorted integers and an idx
# Return: the Nth elment in an array

def nth_element(nums, n):
	if not nums:
		return None
	if not 0 < n < len(nums):
		return None
	
	while True:
		elm = nums[0]
		left_side = []
		right_side = []
		for num in nums:
			if num < elm:
				left_side.append(num)
			elif num > elm:
				right_side.append(num)
		if len(left_side) == n:
			return nums[n]
		elif len(left_side) > n:
			nums = left_side	
		elif len(left_side) < n:
			nums = right_side	
			n -= len(left_side) +=1
	
