# Name:
# Student number:

# A Ring is a double-linked list of which the last node is connected to the first.
# Instead of having a "head" of the list, the Ring has a "current" node.
# By "rotating" the ring, the "current" node moves to a different node. Since the
# ring has no beginning and no end, you can endlessly rotate the ring.
# Each node in the ring has a previous node and a next node. Rotating with a
# positive number of steps follows the nextnode reference as many times as there
# are steps. Negative values for the number of steps rotate by following the
# prevnode references.
# The length of a ring, which is the number of nodes in the ring, you can get
# using the len() function.
# A SortedRing is defined as a ring where all the nodes are added in a way that
# the values are in increasing order (whereby the node with the highest value has
# the node with the lowest value as next node).
# Implement the SortedRing, which inherits from the regular Ring.

class RingNode:
    def __init__( self, value, prevnode=None, nextnode=None ):
        self.value = value
        self.prevnode = prevnode
        self.nextnode = nextnode
    def __repr__( self ):
        return f"RingNode({self.value},prev:{self.prevnode.value},next:{self.nextnode.value})"


class Ring:

    def __init__( self ):
        self.current = None
        self.numnodes = 0
        
    def __len__( self ):
        return self.numnodes

    # Adds a new node to the ring with the given value. The new node
    # is added where self.current is pointing, and the old self.current
    # is the next node for the new node.
    def add( self, value ):
        if self.current == None:
            node = RingNode( value )
            node.prevnode = node
            node.nextnode = node
        else:    
            node = RingNode( value, self.current.prevnode, self.current )
            self.current.prevnode.nextnode = node
            self.current.prevnode = node
        self.current = node
        self.numnodes += 1

    # Rotates the ring the given number of steps. A positive number of
    # steps rotates in the direction of the next nodes, a negative number
    # in the direction of the previous node.
    def rotate( self, steps=1 ):
        if self.current == None:
            return
        if steps > 0:
            while steps > 0:
                self.current = self.current.nextnode
                steps -= 1
        else:
            while steps < 0:
                self.current = self.current.prevnode
                steps += 1

    # Represents the ring as the list of values stored in the ring, 
    # starting with self.current and then, in sequence, the values
    # you find when following the next nodes.
    def __repr__( self ):
        vlist = []
        cur = self.current
        while True:
            vlist.append( str( cur.value ) )
            cur = cur.nextnode
            if cur == self.current:
                break
        s = ",".join( vlist )
        return f"Ring({s})"


class SortedRing( Ring ):
    pass


def main():
    ring = SortedRing()
    ring.add(3)
    print( ring )               # Ring(3)
    ring.add(1)
    print( ring )               # Ring(1,3)
    ring.add(5)
    print( ring )               # Ring(5,1,3)
    ring.add(2)
    print( ring )               # Ring(2,3,5,1)
    ring.add(4)
    print( ring )               # Ring(4,5,1,2,3)
    ring.rotate(2)             
    print(ring)                 # Ring(1,2,3,4,5)

    ring = SortedRing()
    ring.add(5)
    ring.add(3)
    ring.add(8)
    ring.add(4)
    ring.add(5)
    ring.add(3)
    ring.add(7)
    ring.add(6)
    print(ring)                 # Ring(6,7,8,3,3,4,5,5)
    ring.rotate(-5)
    print(ring)                 # Ring(3,3,4,5,5,6,7,8)

    ring = SortedRing()
    ring.add(1)
    ring.add(1)
    ring.add(1)
    ring.add(1)
    print(ring)                 # Ring(1,1,1,1)
    ring.add(2)
    print(ring)                 # Ring(2,1,1,1,1)


if __name__ == "__main__":
    main()