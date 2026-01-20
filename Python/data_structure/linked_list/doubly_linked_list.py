class Node:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head # type: ignore
        if self.head is not None:
            self.head.prev = new_node # type: ignore
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node # type: ignore
        new_node.prev = temp # type: ignore
        
    def delete_at_begining(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
            
    def delete_at_end(self):
        if not self.head:
            return
        temp = self.head
        if not temp.next:
            self.head = None
            return
        while temp.next:
            temp = temp.next
        temp.prev.next = None  # type: ignore
        
    def search_for_data(self, data):
        temp = self.head
        count = 0
        while temp:
            if temp.data == data:
                return count
            temp = temp.next
            count += 1
        return 'not found'
    
    def search_for_index(self, index):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.data
            temp = temp.next
            count += 1
        return 'not found'
    
    def lenght(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count
    
    def print_forward(self):
        temp = self.head
        stringfy = ''
        while temp:
            arrowR = ' <-> '
            arrowL = ''
            if temp.next is None:
                arrowR = f' <-> {temp.next}'
            if temp.prev is None:
                arrowL = f'{temp.prev} <-> '
            stringfy += arrowL + str(temp.data) + arrowR
            temp = temp.next
        return stringfy
    
    

dll = DoublyLinkedList()
dll.insert_at_begining(3)
dll.insert_at_begining(2)
dll.insert_at_begining(1)
dll.insert_at_end(4)
dll.delete_at_begining()
dll.delete_at_end()

print(dll.print_forward())

search_data = 4
print(f'Searched for data: {search_data}, found at index:', dll.search_for_data(search_data))

search_index = 1
print(f'Searched for index: {search_index}, found at data:', dll.search_for_index(search_index))