# Stacks are a data structure that adhere to LIFO

s = []

s.append("backwards")
s.append("sense")
s.append("makes")
s.append("sentence")
s.append("this")

while s:
	print(s.pop())
