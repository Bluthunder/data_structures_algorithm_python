'''
Stack - Data Structure
Stack ADT implementation based on Dynamic array 
Date - 16 November 2023
Author - Bluthunder

'''

class Stack(object):

	def __init__(self,limit = 10):
		self.stk = []
		self.limit = limit
		
	def isEmpty(self):
		return len(self.stk) <= 0
	
	def isFull(self):
		return len(self.stk) >= self.limit
		
	def push(self,element):
		if len(self.stk) >= self.limit:
			self.resize()
		self.stk.append(element)
		print('Stack after push operation',self.stk)
	
	def pop(self):
		if self.isEmpty():
			print('*** STACK UNDERFLOW ***')
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print('*** STACK UNDERFLOW ***')
			
		else:
			return self.stk[-1]
			
			
	def size(self):
		return len(self.stk)
		
	'''
	RESIZING IS BASED ON REPEATED DOUBLING APPROACH. 
	O(n)
	'''
	def resize(self):
		newStk = list(self.stk)
		self.limit = 2*self.limit
		self.stk = newStk
		
		
MyStack = Stack(5)
MyStack.push('10')
MyStack.push('20')
MyStack.push('30')
MyStack.push('40')
MyStack.push('50')
MyStack.push('60')
MyStack.push('70')
MyStack.push('180')
print(MyStack.peek())
			
	
	
		
		
	