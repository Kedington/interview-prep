# Searching Algorithms

# Basic Search Algorithm 
# Best Case: 	O(1)
# Worst Case: 	O(n)
# Memory: 		O(1)
# Searches for first apperance of an elm
# Return: idx if one exists else None

def search(nums, elm):
	for idx in range(len(nums)):
		if nums[idx] == elm:
			return idx 

# Binary Search 
# O(logn)
# O(1)
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
