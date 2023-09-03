# Name:
# Student number:

'''
When trees are used in software, they are often binary trees, but not necessarily 
so. A node in a tree can have any number of branches, if it stores references to 
the branches in, for instance, a list. 

The exercise file contains a class Node, which has a value and a list of nodes.  
The nodes in the list are the roots of the subtrees which form the branches under 
the node. If the list is empty, then the node is a leaf node. 

Two methods in the class Node must be implemented.

The method numnodes() gets no arguments, and returns the number of nodes in the 
(sub)tree of which the node is the root (this includes the node itself).

The method find() gets one argument, namely a value, and returns True if the value 
is found somewhere in the tree, and False otherwise. As there is no ordering in 
the implementation of the tree, you will have to search the entire tree to find 
the value. You can do this using a depth-first search or a breadth-first search 
(your choice).
'''

class Node:
    def __init__( self, value, nodes ):
        self.value = value
        self.nodes = nodes
    def find( self, num ):
        return False
    def numnodes( self ):
        return -1
    def __repr__( self ):
        return f"Node({self.value},{self.nodes})"

def main():
    tree = Node(1,[Node(2,[Node(5,[]),Node(6,[])]),Node(3,[]),Node(4,[])])
    print( tree.numnodes() )            # 6
    for i in range( 10 ):
        print( i, tree.find( i ) )      # False for 0 and 7 and higher,
                                        # True for 1 to 6.
    tree = Node(1,[Node(2,[Node(5,[Node(10,[]),Node(11,[])]),Node(6,[])]),\
        Node(3,[Node(7,[Node(12,[]),Node(13,[]),Node(14,[Node(15,[])])])]),\
        Node(4,[Node(8,[Node(16,[]),Node(17,[Node(20,[])]),Node(18,[]),Node(19,[])]),\
        Node(9,[Node(21,[Node(22,[])])])])])
    print( tree.numnodes() )            # 22
    for i in range( 30 ):
        print( i, tree.find( i ) )      # False for 0 and 23 and higher,
                                        # True for 1 to 22.
    
if __name__ == "__main__":
    main()