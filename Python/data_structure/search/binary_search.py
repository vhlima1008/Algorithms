class Node:
    def __init__(self, data):
        self.prev: Node | None = None
        self.data = data
        self.next: Node | None = None
        
class BinarySearch:
    def __init__(self):
        self.head = None
        
    def insert_array(self, array):
        for item in array:
            node = Node(item)
            node.next = self.head
            self.head = node
        
    def node_counts(self):
        if self.head is None:
            return 'underflow condition'
        
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count
            
    def search_for(self, data):
        if self.head is None:
            return 'underflow condition'
        
        size = int(self.node_counts())
        mid = round(size/2)
        
        
            
    def transverse(self):
        temp = self.head
        stringfy = ''
        while temp:
            space = ', '
            if temp.next is None:
                space = ''
            stringfy += str(temp.data) + space
            temp = temp.next
        return stringfy

binary_search = BinarySearch()

binary_search.insert_array([1,2,3,4,5])

print(binary_search.transverse())

