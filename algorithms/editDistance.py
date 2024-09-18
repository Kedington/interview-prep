# Edit Distance

# Given two strings str1 and str2
# Find minimum number of edits required to convert a str1 into str2
# Operations: Insert Remove Replace 

# Initial Thoughts:
# 	If length of str1 is less than length of str2 we will need to insert len(str2)-len(str1) characters
# 	The inverse is also true if len(str1) > len(str2) we need to remove len(str1)-len(str2) characters
# 	We want to find the characters that match and insert and remove characters so that they are in the right position
#	If a character is in the right place at the right index make no adjustments to it or things that would adjust it
# 	Also when characters are in the same place it breaks down into a simpler problem where those characters are not in the string
# 	If two strings are the same length you still might need to replace and insert ex:
#	'cab' 'abc' rather than replace 3 times, we remove 'c' and insert 'c' at the end (2 operations)
# 	'ab' 'def'
# 	The amount of operations to get from str1 -> str2 is equivlent to the amount of operations from str2 -> str1

test_cases = [{('', ''): 0, ('a', ''): 1, ('', 'a'): 1, ('a', 'b'): 1}]

def edit_distance(str1, str2):
	len_str1 = len(str1)
	len_str2 = len(str2)
	
	result_matrix = [[0 for x in range(len_str1+1)] for y in range(len_str2+1)]
	for y in range(len_str2+1):
		for x in range(len_str1+1):
			if y == 0:
				result_matrix[y][x] = x
			elif x == 0:
				result_matrix[y][x] = y
			elif str1[x-1] == str2[y-1]:
				result_matrix[y][x] = result_matrix[y-1][x-1]
			else:
				result_matrix[y][x] = 1 + min(result_matrix[y-1][x],
									  		  result_matrix[y][x-1],
									  		  result_matrix[y-1][x-1])
	return result_matrix[len_str2][len_str1]

def editDistance(str1, str2):
	if not str1 or not str2:
		return len(str1) or len(str2)

	# Remove any characters that are at their correct idx
	short_len = min(len(str1), len(str2))
	new_str1 = ''
	new_str2 = ''
	for idx in range(short_len):
		if not str1[idx] == str2[idx]:
			new_str1 = str1[idx]
			new_str2 = str2[idx]
	
	# In the case where they share no characters 
	chars_str1 = set()	
	chars_str2 = set()
	for char in str1:
		char_str1.add(char)
	for char in str2:
		char_str2.add(char)

	if not char_str1.union(char_str2):
		if len(str1) <= len(str2):
			return len(str2)
		else:
			return len(str1)
	
	 
