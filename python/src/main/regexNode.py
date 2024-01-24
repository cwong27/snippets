import sys
import binascii

class Node(object):
	def __init__(self, value, end=False):
		self.end = False
		self.value = value
		self.children = set()

	def add_child(self, node):
		self.children.add(node)

	def set_end(self, end):
		self.end = end

	def matchesChild(self, value):
		for child in self.children:
			if child.value == value:
				return child
		return None

root = Node('ROOT')

def printTree():
	current = root
	queue = []
	queue.put(current)
	while not queue.empty():
		current = queue.get()
		print (current.value)
		for child in current.children:
			queue.put(child)

def addString(input): 
	inputBytes = input.encode('utf-8')
	#print binascii.hexlify(inputBytes)
	if len(inputBytes) == 0:
		return
	current = root
	for inputByte in inputBytes:
		child = current.matchesChild(inputByte)
		if child:
			current = child
		else:
			child = Node(inputByte)
			current.add_child(child)
			current = child
	current.set_end(True)

def matchString(input):
	inputBytes = input.encode('utf-8')
	if len(inputBytes) == 0:
		print ('No match')
		return
	current = root
	for inputByte in inputBytes:
		child = current.matchesChild(inputByte)
		if not child:
			current = root
		elif child.end:
			print (f"Match found: {input}")
			return;
		else:
			current = child
	print ('No match found!')


def main(argv):
	print ('Regex with nodes')
	addString('Whs')
	addString('Whg')
	addString('abcdefg')
	addString('124')
	addString('abc12345')
	addString('http://')
	addString('10.')
	#printTree()

	matchString('sjdfjksWhs')
	matchString('abc')
	matchString('124')
	matchString('sdjhfWhgsjk')
	matchString('82eheuhg8erg4124kwfmkmnfie')
	matchString('____abc12345++++')
	matchString('abcabcabcdefgdfgdfg')
	matchString('http://good.com')
	matchString('https://good.com')
	matchString('https://10.0.0.1')

if __name__ == "__main__":
	main(sys.argv[1:])
