def max_frame_sum(matrix, frameSize):
	N = len(matrix)
	M = len(matrix[0])
	frame_sums = {}
	for y in range(N):
		for x in range(M):
			if x + frameSize-1 < M and y + frameSize-1 < N:
				frame_sums[(x,y)] = 0
			for frame in frame_sums:
				if is_in_frame(x,y, frame[0], frame[1], frameSize):
					frame_sums[frame] += matrix[y][x]
	max_sum = max(frame_sums.values())
	max_frames = [frame for frame, sum in frame_sums.items() if sum == max_sum]
	print(frame_sums)
	print(max_frames)
	output = set()
	for y in range(N):
		for x in range(M):
			for frame in max_frames:
				if is_in_frame(x, y, frame[0], frame[1], frameSize):
					output.add(matrix[y][x])

	print(output)
	return sum(output)

def is_in_frame(x, y, frame_x, frame_y, frameSize):
	if x == frame_x or x == frame_x+(frameSize-1):
		if frame_y <= y < frame_y+frameSize:
			return True
	elif y == frame_y or y == frame_y+(frameSize-1):
		if frame_x <= x < frame_x+frameSize:
			return True
	return False
				 

max_frame_sum([[1,2],[3,4]], 1)
max_frame_sum([[1,2],[3,4]], 2)
print(max_frame_sum([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
         2))
print(max_frame_sum([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        3))
