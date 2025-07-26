class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################
    
    def find_middle_node(self):
        if self.head == None and self.tail == None:
            return None
        
        if self.head.next == None and self.tail.next == None:
            return self.head
            
        if self.head.next.next == None and self.tail.next == None:
            return self.head
            
        else:
            slow = self.head
            fast = self.head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        
        return slow
        
        




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""