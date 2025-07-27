# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
    
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
# class Queue:
    ## WRITE QUEUE CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################
class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

my_queue = Queue(4)

print('First:', my_queue.first.value)
print('Last:', my_queue.last.value)
print('Length:', my_queue.length)


"""
    EXPECTED OUTPUT:
    ----------------
    First: 4
    Last: 4
    Length: 1

"""