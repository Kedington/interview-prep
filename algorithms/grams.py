# Takes two words -> return True if anagrams or False
# Time complexity: O(n) where n is the input length of the string
# Memory complexity: O(n) where n is the length of the string
# Store the charactes and their frequency in a dictionary
# Then decrement them on the way out

def isAnagram(s: str, t: str) -> bool:
   letter_count = defaultdict(int)
   for char in s:
	hash_map[char] += 1

   for char in t:
       if char not in letter_count:
           return False
       elif char in letter_count and letter_count[char] == 1:
           letter_count.pop(char)
       else:
           letter_count -= 1
   return not letter_count
      

