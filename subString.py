def sub_string(s):
	sub_strings = set()
	for idx in range(len(s)):
		for idx2 in range(idx, len(s)+1):
			sub_strings.add(s[idx:idx2])
	return sub_strings

def longest_substring(s1, s2):
	sub_strings = sub_string(s1).intersection(sub_string(s2))
	print(sub_strings)
	long_string = ''
	for string in sub_strings:
		if len(string) > len(long_string):
			long_string = string
	return long_string

