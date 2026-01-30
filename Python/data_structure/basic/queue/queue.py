class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    
    def dequeue(self):
        if self.front is None:
            return "underflow condition"
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        value = temp.data
        del temp
        return value
    
    def peek(self):
        if self.front is None:
            return "underflow condition"
        return self.front.data
    
    def transverse(self):
        temp = self.front
        stringfy = ''
        while temp:
            arrow = ' <- '
            if temp.next is None:
                arrow = ''
            stringfy += str(temp.data) + arrow
            temp = temp.next
        return stringfy
    
queue = Queue()

print('(front/exit)',queue.transverse(),'(rear/entrance)','\n')
print('peek (first element):',queue.peek())
print()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')
queue.enqueue('F')
print('Added:','A')
print('Added:','B')
print('Added:','C')
print('Added:','D')
print('Added:','E')
print('Added:','F')
print()

print('(front/exit)',queue.transverse(),'(rear/entrance)','\n')
print('peek (first element):',queue.peek())
print()

print('Removed:',queue.dequeue())
print('Removed:',queue.dequeue())
print('Removed:',queue.dequeue())
print()

print('(front/exit)',queue.transverse(),'(rear/entrance)','\n')
print('peek (first element):',queue.peek())