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

newNode = Node()
newNode.data = "하하"
newNode.link = node2.link   # 정연의 링크
node2.link = newNode

current = node1
print(current.data, end = ' ')
while current.link != None :
	 current = current.link
	 print(current.data, end = ' ')
