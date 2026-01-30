class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data): 
        temp = Node(data)
        temp.next = self.top
        self.top = temp
        
    def pop(self):
        if self.top is None:
            raise Exception("underflow condition")
        temp = self.top
        self.top = self.top.next
        value = temp.data
        del temp
        return value
    
    def peek(self):
        if self.top is None:
            raise Exception("underflow condition")
        return self.top.data
    
    def size(self):
        temp = self.top
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count
            
    def transverse(self):
        if self.top is None:
            raise Exception("underflow condition")
        temp = self.top
        stringfy = ''
        count = self.size() - 1
        while temp:
            break_point = f' {count}\n'
            stringfy += str(temp.data) + break_point
            temp = temp.next
            count -= 1
        return stringfy

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
stack.push("d")
stack.pop()

print(stack.transverse())
print('peek:',stack.peek())