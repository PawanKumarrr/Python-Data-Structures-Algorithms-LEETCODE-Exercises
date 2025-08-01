class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    ## WRITE ENQUEUE METHOD HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################

    def enqueue(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.first = new_Node
            self.last = new_Node
            
        else:
            self.last.next = new_Node
            self.last = new_Node
        
        self.length += 1


my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""