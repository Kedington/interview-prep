def flipMatrix(matrix):
	n = len(matrix)/2
	q = len(matrix) - 1
	output = 0
	for i in range(n):
		for j in range(n):
			output += max([matrix[i][j], matrix[i][q-j], matrix[q][j]
		output += max(matrix[idx][idx],
