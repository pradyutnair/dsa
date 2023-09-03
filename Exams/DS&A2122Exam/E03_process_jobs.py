# Name:
# Student number:

'''
JobList is a SingleLinkedList, exactly as it appears in the notebooks, consisting of SingleNodes. 
The only extra method in JobList, which you have to create, is process_request().
process_request() gets three parameters (apart from self): request (string), job (string), 
and priority (string). There are three possible values for request, namely "add", "remove", 
and "list". There are two possible values for priority, namely "low" and "high".
If the request is "add", you add the string contained in job to the linked list. If the priority 
is "low", you add the job to the end of the linked list. If the priority is "high", you add the 
job to the start of the linked list. The method returns a string "added: " plus the job. Note 
that when a high-priority job is added to the list, you can just attach it to the head – you do 
not have to insert it after all other high-priority jobs. Therefore you do not need to store the 
priority with a job.
If the request is "remove", you remove one job from the list, namely the one at the start. 
The method returns a string "removed: " plus the job that was removed. If there were no jobs in 
the list, the method only returns the string: "removed: Nothing".
If the request is "list", the method returns the string: "list: " plus all the jobs in the linked 
list, starting at the start, separated by commas.
'''

ADD = 'add'
REMOVE = 'remove'
LIST = 'list'
LOW = 'low'
HIGH = 'high'

class SingleNode:
    def __init__( self, value, nextnode ):
        self.value = value
        self.nextnode = nextnode
        
class JobList:
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
    def process_request( self, request, job="", priority=LOW ):
        return "Unknown command"
    
def main():
    joblist = JobList()
    print( joblist.process_request( ADD, "orange" ) )       # added: orange (low priority)
    print( joblist.process_request( ADD, "pear" ) )         # added: pear (low priority)
    print( joblist.process_request( ADD, "apple", HIGH ) )  # added: apple (high priority) 
    print( joblist.process_request( ADD, "banana", HIGH ) ) # added: banana (high priority)
    print( joblist.process_request( LIST ) )                # list: banana, apple, orange, pear 
    print( joblist.process_request( REMOVE ) )              # removed: banana
    print( joblist.process_request( LIST ) )                # list: apple, orange, pear 
    print( joblist.process_request( REMOVE ) )              # removed: apple 
    print( joblist.process_request( REMOVE ) )              # removed: orange
    print( joblist.process_request( REMOVE ) )              # removed: pear
    print( joblist.process_request( REMOVE ) )              # removed: Nothing 
    
if __name__ == "__main__":
    main()
