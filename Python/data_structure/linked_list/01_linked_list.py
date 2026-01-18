class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        
        idx = self.head
        while idx.next:
            idx = idx.next
        idx.next = Node(data, None)
        
    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
        
        
    def show(self):
        if self.head is None:
            return 'linked list is empty'

        idx = self.head
        stringfy = ''
        while idx:
            arrow = ' -> '
            if idx.next is None:
                arrow = f' -> {idx.next}'
            stringfy += str(idx.data) + arrow
            idx = idx.next
        return stringfy
    
    def lenght(self):
        idx = self.head
        count = 0
        while idx:
            idx = idx.next
            count += 1
        return count
    
    def remove_at(self, index):
        if index < 0 or index > self.lenght():
            return f'invalid index: {index}'
        if index == 0:
            self.head = self.head.next # type: ignore
            return
        
        count = 0
        idx = self.head
        while idx:
            if count == index - 1:
                idx.next = idx.next.next  # type: ignore
                break
            idx = idx.next
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 or index > self.lenght():
            return f'invalid index: {index}'
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        idx = self.head
        while idx:
            if count == index - 1:
                node = Node(data, idx.next)
                idx.next = node
                break
            idx = idx.next
            count += 1                
    
    def search_for(self, data):
        count = 0
        idx = self.head
        while idx:
            if idx.data == data:
                return count
            idx = idx.next
            count += 1
        return -1
    
    def insert_after_value(self, value, value_after):
        idx = self.head
        while idx:
            if idx.data == value:
                node = Node(value_after, idx.next)
                idx.next = node
                return
            idx = idx.next
        return 'not found data before'
    
    def remove_by_value(self, data):
        index = self.search_for(data)
        self.remove_at(index)
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_end(2)
    ll.insert_at_begining(3)
    ll.insert_values([4,5,6,7])
    ll.remove_at(0)
    ll.insert_at(1, 8)
    ll.insert_after_value(8,9)
    ll.remove_by_value(9)
    
    print('linked list:',ll.show())
    
    n = 8
    print(f'searched value: {n} position:',ll.search_for(n))
    print('length:',ll.lenght())

