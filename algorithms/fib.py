def fib(n):
	if n in [0,1]:
		return 1
	left, right = 1, 1
	for _ in range(n-1):
		left, right = left+right, left
	return left

def fib_rec(n):
	if n in [0,1]:
		return 1
	return fib(n-1) + fib(n-2)


def fib_mem(n, cache={}):
	if n in cache:
		return cache[n]
	if n in [0,1]:
		cache[n] = 1
		return 1
	cache[n] = fib(n-1) + fib(n-2)
	return cache[n] 

