# Queues are a data structure that adhere to FIFO

s = []

s.insert(0, "This")
s.insert(0, "sentence")
s.insert(0, "comes")
s.insert(0, "out")
s.insert(0, "the")
s.insert(0, "same")
s.insert(0, "way")
s.insert(0, "it")
s.insert(0, "went")
s.insert(0, "in")

while s:
	print(s.pop())
