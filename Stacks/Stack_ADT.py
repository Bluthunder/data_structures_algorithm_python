'''
Stack - Data Structure
Stack ADT implementation based on simple array 
Date - 16 November 2023
Author - Bluthunder

'''

class Stack(object):

	def __init__(self,limit=10):
		self.stk = []
		self.limit = limit
	
	# This would check if 
	def isEmpty(self):
		print(len(self.stk))
		return len(self.stk) <= 0
		
	def isFull(self):
		print(f" Stack is {len(self.stk)},{self.limit}")
		return len(self.stk) >= self.limit
		
	
	def push(self,element):
		#if self.isFull() == True: This can also be on implementation. 
		if len(self.stk) >= self.limit:
			print(" *** STACK OVERFLOW *** ")
		else:
			self.stk.append(element)
			print("Stack After push operation",self.stk)
			
	def pop(self):
		# if self.isEmpty == True:
		if len(self.stk) <= 0:
			print(" *** STACK UNDERFLOW *** ")
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print("*** STACK UNDERFLOW *** ")
			return 0
		else:
			return self.stk[-1]
	
	def size(self):
		return len(self.stk)
		
StackObject = Stack(5)
StackObject.isEmpty()
StackObject.push("Name")
StackObject.push("Age")
StackObject.push("IN")
StackObject.push("oio")
StackObject.push("9")
print(StackObject.pop())
print(StackObject.peek())
print(StackObject.size())

