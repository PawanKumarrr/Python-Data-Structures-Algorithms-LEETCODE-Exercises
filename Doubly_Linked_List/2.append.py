class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    ## WRITE APPEND METHOD HERE ##
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################
    def append(self, value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
            return True
        
        else:
            self.tail.next = new_Node
            new_Node.prev = self.tail
            self.tail = self.tail.next
            self.length = self.length+1
            return True
        
        return False


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2
    
"""
