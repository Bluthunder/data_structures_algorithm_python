''' 
Need to comeback on this
'''
class Node:
	def __init__(self):
		self.data = None
		self.next = None
		
	def setData(self, data):
		self.data = data
	
	def getData(self):
		return self.data
	
	def setNext(self, next):
		self.next = next
	
	def getNext(self):
		return self.next
		
	def hasNext(self):
		return self.next != None
		
class Stack(object):
	
	def __init__(self, data = None):
		self.head = None
		if data:
			for data in data:
				self.push(data)
	
	def push(self, data):
		temp = Node()
		temp.data = data
		temp = self.head
		self.head = temp
	
	def pop(self):
		if self.head is None:
			raise IndexError
		temp = self.head.data
		self.head = self.head.next
		return temp
		
	def peek(self):
		if self.head is None:
			raise IndexError
		return self.head.data
		
OurList = ['First', 'Second', 'Third', 'Fourth']
OurStack = Stack(OurList)
print(OurStack.pop())
			
	