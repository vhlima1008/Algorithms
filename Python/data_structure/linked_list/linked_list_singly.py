class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        
    def insert_at_end(self, data):
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = Node(data)
                break
            temp = temp.next
    
    def insert_at(self, data, position):
        pass
            
    def delete_from_begining(self):
        if self.head is None:
            raise Exception('underflow condition')
        self.head = self.head.next
    
    def delete_from_end(self):
        pass
        
    def delete_from(self, position):
        pass
    
    def search_for(self, data):
        pass
    
    def update_at(self, data, position):
        pass

    def transverse(self):
        pass
    
    def revert(self):
        pass
    
    def show(self):
        if self.head is None:
            return 'underflow condition'
        temp = self.head
        stringfy = ''
        while temp:
            arrow = ' -> '
            if temp.next is None:
                arrow = ''
            stringfy += str(temp.data) + arrow
            temp = temp.next
        return stringfy
            
linked_list = LinkedList()
linked_list.insert_at_begining('a')
linked_list.insert_at_begining('b')
linked_list.insert_at_begining('c')
linked_list.insert_at_end('d')
linked_list.insert_at_end('e')
linked_list.insert_at_end('f')

print(linked_list.show())
        