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
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
    
    def insert_at(self, data, position):
        if position < 0 or position > self.count_nodes():
            return f'out of touch'
        if position == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        temp = self.head
        while temp:
            if count == position - 1:
                node = Node(data)
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next
            count += 1
            
    def delete_from_begining(self):
        if self.head is None:
            return 'underflow condition'
        
        self.head = self.head.next
    
    def delete_from_end(self):
        if self.head is None:
            return 'underflow condition'
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None
        
    def delete_from(self, position):
        if position < 0 or position > self.count_nodes():
            return f'out of touch'
        if position == 0:
            self.delete_from_begining()
            return
        
        count = 0
        temp = self.head
        while temp:
            if count == position - 1:
                temp.next = temp.next.next  # type: ignore
                break
            temp = temp.next
            count += 1
    
    def search_for(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def update_at(self, data, position):
        if self.head is None:
            return 'underflow condition'
        if position < 0 or position > self.count_nodes() - 1:
            return 'out of range'
        
        count = 0
        temp = self.head
        while temp:
            if position == count:
                temp.data = data
                return
            count += 1
            temp = temp.next
    
    def revert(self):
        if self.head is None:
            return 'underflow condition'
        curr = self.head
        prev = None
        while curr:
            node = curr.next
            curr.next = prev # type: ignore
            prev = curr
            curr = node
        self.head = prev
    
    def transverse(self):
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
linked_list.insert_at_begining('begining A')
linked_list.insert_at_begining('begining B')
linked_list.insert_at_begining('Begining C')
linked_list.insert_at_end('end D')
linked_list.insert_at_end('end E')
linked_list.insert_at_end('end F')
linked_list.delete_from_begining()
linked_list.delete_from_end()
linked_list.delete_from_end()
linked_list.delete_from_end()
linked_list.update_at('update G', 2)
linked_list.delete_from(1)
linked_list.insert_at('insert H', 1)
linked_list.insert_at('insert I', 0)
linked_list.insert_at('insert J', 1)
linked_list.revert()


print('linked list:',linked_list.transverse())
print('size:',linked_list.count_nodes())
searched_value = 'insert H'
found_result = f'searched for "{searched_value}": not found'
if linked_list.search_for(searched_value):
    found_result = f'searched for "{searched_value}": found'    
print(found_result)