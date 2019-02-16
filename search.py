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
