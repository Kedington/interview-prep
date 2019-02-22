# Binary Search Tree

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Tree:
	def __init__(self, val):
		self.root = TreeNode(val)
	
	def add_node(self, val):
		next_node = self.root

		while next_node:
			if val < next_node.val:
				if not next_node.left:
					next_node.left = TreeNode(val)
					return
				else:
					next_node = next_node.left
			elif val > next_node.val:
				if not next_node.right:
					next_node.right = TreeNode(val)	
					return
				else:
					next_node = next_node.right
			
	def print_tree(self):
		stack = []
		stack.append(self.root)
				
		while stack:
			curr = stack.pop()
			print(curr.val)
			if curr.left:
				stack.insert(0, curr.left)
			if curr.right:
				stack.insert(0, curr.right)
