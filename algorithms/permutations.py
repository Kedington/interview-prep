def permute(nums):
    # Base case: If the list is empty, return an empty list
    if len(nums) == 0:
        return []
    
    # Base case: If the list has one element, return a list with one permutation
    if len(nums) == 1:
        return [nums]
    
    # List to store all the permutations
    permutations = []
    
    # Iterate through the list, treating each element as the first in the permutation
    for i in range(len(nums)):
        # Extract the current element
        current = nums[i]
        # Get the remaining elements
        remaining = nums[:i] + nums[i+1:]
        
        # Recursively generate permutations of the remaining elements
        for p in permute(remaining):
            # Add the current element at the beginning of each permutation of the remaining elements
            permutations.append([current] + p)
    
    return permutations

# Example usage
nums = [1, 2, 3]
result = permute(nums)
for perm in result:
    print(perm)

