def bs(nums, target): 
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = (right + left) // 2 
		if nums[mid] == target:
			return True
		
		elif nums[mid] < target: 
			left = mid+1
		else:
			right = mid-1  
	return False



print(bs([], 1) == False)
print(bs([0], 1) == False)
print(bs([0,2], 1) == False)
print(bs([0,2,3,4], 1) == False)
print(bs([1], 1) == True)
assert bs([1,2], 1) == True
assert bs([1,2,3], 1) == True
assert bs([1,2,3], 2) == True
assert bs([1,2,3], 3) == True
assert bs([1,2,3,4], 1) == True
assert bs([1,2,3,4], 2) == True
assert bs([1,2,3,4], 3) == True
assert bs([1,2,3,4], 4) == True

