# Name:
# Student number:

'''
In this exercise you will be keeping track of the order in which people
arrive to a queue.
The code given for this exercise contains two classes: SingleNode and Queue. 
Queue is actually a SingleLinkedList, as introduced in the course. The code 
for this class (which is taken directly from the notebooks) contains methods
__init__(), add(), append(), and remove(). add() adds a new SingleNode at 
the head of the Queue, append() appends a new SingleNode at the tail of the 
Queue, and remove() removes the SingleNode which is at the head of the Queue
(if the Queue is not empty, otherwise it will generate an exception). 
The Queue will be used to keep track of a line of people. New arrivals will 
either go to the tail of the queue, or will be placed at the head of the 
queue (depending on whether add() or append() is used). Someone may get 
removed from the queue; if so, this is done with the remove() method, so 
they will be removed from the head of the queue.
In this exercise you have to implement the method orderOfArrival() for the 
Queue, which returns a string that tells us the order in which people have 
arrived to join the queue (separating the names of the people with the word
"then"), regardless of whether they were added to its head or its tail.
When creating your solution, you are allowed to change the existing methods 
of the class Queue (in fact, that is pretty much necessary). You may also 
make changes to the SingleNode class if you want. You may assume that the 
remove() method is only used when there is at least one person in the queue.
'''

class SingleNode:
    def __init__( self, value, nextnode ):
        self.value = value
        self.nextnode = nextnode
        
class Queue:
    def __init__( self ):
        self.head = None
        self.tail = None
    def add( self, value ):
        node = SingleNode( value, self.head )
        self.head = node
        if self.tail == None:
            self.tail = self.head
    def remove( self ):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nextnode
    def append( self, value ):
        node = SingleNode( value, None )
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.nextnode = node
            self.tail = node
    def orderOfArrival( self ):
        order = ""
        return order

queue1 = Queue()
queue1.add("Bobby")
queue1.add("Xerxes")
queue1.add("Astrid")
queue1.add("Angela")
queue1.add("George")

queue2 = Queue()
queue2.append("Bobby")
queue2.append("Xerxes")
queue2.append("Astrid")
queue2.append("Angela")
queue2.append("George")

queue3 = Queue()
queue3.append("Bobby")
queue3.add("Xerxes")
queue3.add("Astrid")
queue3.append("Angela")
queue3.add("George")

queue4 = Queue()
queue4.append("Bobby")
queue4.add("Xerxes")
queue4.add("Astrid")
queue4.append("Angela")
queue4.add("George")
queue4.remove()
queue4.remove()

print( queue1.orderOfArrival() ) # Bobby then Xerxes then Astrid then Angela then George
print( queue2.orderOfArrival() ) # Bobby then Xerxes then Astrid then Angela then George
print( queue3.orderOfArrival() ) # Bobby then Xerxes then Astrid then Angela then George
print( queue4.orderOfArrival() ) # Bobby then Xerxes then Angela
