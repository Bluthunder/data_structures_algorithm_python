'''
Node of Singly Linked List
'''

class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
		

class LinkedList:
	
	'''
	This creates an linkedlist with single node
	
	def __init__(self, data):
		new_node = Node(data)
		self.head = new_node
		self.tail = new_node
		self.length = 1
		
	'''
	
	# This will create an empty linkedList 
	
	def __init__(self):
		self.head = None
		self.next = None
		self.length = 0
	
	def __str__(self):
		temp_node = self.head
		result = ""
		while temp_node is not None:
			result += str(temp_node.value)
			if temp_node.next is not None:
				result += ' -> '
			temp_node = temp_node.next
		return result
			
	def append(self,value):
		new_node = Node(value)
		
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
		self.length += 1 
	
	
	def prepend(self, value):
		new_node = Node(value)
		
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			
		else:
			new_node.next = self.head
			self.head = new_node
			
		self.length += 1
		
	
	def get(self, index):
		
		if index < 0 or index >= self.length:
			return None
			
		temp_node = self.head
		
		for _ in range(index):
			temp_node = temp_node.next
		return temp_node
		
	def setValue(self, index, value):
		temp_node = self.get(index)
		if temp_node:
			temp_node.value = value
		return temp_node
	

	def insert(self, index, value):
		new_node = Node(value)
		
		if index < 0 or index > self.length:
			return False
		
		if index == 0:
			return self.prepend(value)
			
		if index == self.length:
			return self.append(value)
			
		temp = self.get(index-1)
		new_node.next = temp.next
		temp.next = new_node
		self.length += 1
		return True
		
		
	
		

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.get(2)
ll1.prepend(0)
print(ll1)
ll1.insert(3,10)
print(ll1)
ll1.setValue(3,11)
print(ll1)
