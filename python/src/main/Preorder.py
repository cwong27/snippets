import sys

class BinaryTreeNode:
	def __init__(self, value, left=None, right=None):
		self.value = value;
		self.left = None
		self.right = None
	
def Preorder(node):
	if node is None:
		return
	print node.value
	Preorder(node.left)
	Preorder(node.right)

def main(argv):
	a = BinaryTreeNode("A")
	b = BinaryTreeNode("B")
	c = BinaryTreeNode("C")
	d = BinaryTreeNode("D")
	e = BinaryTreeNode("E")
	f = BinaryTreeNode("F")
	g = BinaryTreeNode("G")
	h = BinaryTreeNode("H")
	i = BinaryTreeNode("I")

	f.left, f.right = b, g
	b.left, b.right = a, d
	g.right = i
	i.left = h
	d.left, d.right = c, e
	
	Preorder(f)
	exit()

if __name__ == "__main__":
	main(sys.argv[1:])
