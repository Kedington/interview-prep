import heapq

class State:
	def __init__(self, state):
		self.state = state
		self.min_zero_heap = [idx for idx, val in enumerate(self.state) if val == 0]
		heapq.heapify(self.min_zero_heap)

	def L(self):
		# Set smallest 0 to 1 or do nothing
		if self.min_zero_heap:
			min_zero_index =  heapq.heappop(self.min_zero_heap)
			self.state[min_zero_index] = 1

	def C(self, index):
		# Set index to 0 regadless of value
		if self.state[index] == 1:
			self.state[index] = 0
			heapq.heappush(self.min_zero_heap, index)

	def return_state(self):
		return "".join([str(val) for val in self.state])

	
def run_operations(state, operations):
	state_obj = State(state)
	for operation in operations:
		if operation == "L":
			state_obj.L()
		elif operation.startswith("C"):
			state_obj.C(int(operation[1:]))
	return state_obj.return_state()
