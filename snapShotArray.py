class SnapshotArray:
	def __init__(self, length):
		self.length = length
		self.arr = [None] * length
		self.snapshots = {}
		self.num_of_snapshots = 0

	def get(self, index):
		return self.arr[index]

	def put(self, index, value):
		if self.snapshots:
			self.snapshots[self.num_of_snapshots][index] = value
		self.arr[index] = value 
		
	def take_snapshot(self):
		if not self.snapshots:
			self.snapshots[self.num_of_snapshots] = self.arr.copy()	

		self.num_of_snapshots += 1
		self.snapshots[self.num_of_snapshots] = {}
		return self.num_of_snapshots - 1

	def get_snapshot(self, index, token):
		for snap_idx in range(token, 0, -1):
			if index in self.snapshots[snap_idx]:
				return self.snapshots[snap_idx][index]
		return self.snapshots[0][index]
		
