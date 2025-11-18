from queue import Queue

class ThisQueue:
    def __init__(self, maxLen=10):
        self.queue = Queue(maxsize=maxLen)
        
    def insert(self, a):
        if not self.queue.full():
            self.queue.put(a)

    def remove(self):
        if not self.queue.empty():
            self.queue.get()

    def isALot(self):
        return self.queue.full()
    
    def isClean(self):
        return self.queue.empty()
    
    def lenght(self):
        return self.queue.qsize()
    
    def maxLenght(self):
        return self.queue.maxsize
    
    def __str__(self):
        return f'This Queue: current={self.lenght()}, max={self.maxLenght()}'
    
myQueue = ThisQueue(5) # Max Size of Queue is set to 5

myQueue.insert(1) # first add 1, first go out
myQueue.insert(2) # second add 2, second go out 
myQueue.insert(3) # third add 3, third go out

myQueue.remove() # the queue walked, the second will be the first

print(myQueue.isClean()) # isn't clean: false
print(myQueue.isALot()) # isn't full: false

print(myQueue) # will print the size: 2, and the max-size of queue: 5

# by Victor Hugo Lima