
"""
	싱글 연결리스트(Singly Linked List)


"""

class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

node1 = Node()
node1.data = "유재석"

node2 = Node()
node2.data = "강호동"
node1.link = node2

node3 = Node()
node3.data = "신동엽"
node2.link = node3

node4 = Node()
node4.data = "서장훈"
node3.link = node4

node5 = Node()
node5.data = "김희철"
node4.link = node5

print(node1.data, end = ' ')
print(node1.link.data, end = ' ')
print(node1.link.link.data, end = ' ')
print(node1.link.link.link.data, end = ' ')
print(node1.link.link.link.link.data, end = ' ')

