# Name:
# Student number:

# Item is the general Item class. Set the optional attribute to True if you want
# your code to be tested for the optional challenge.
class Item:
    def __init__( self, name="" ):
        self.name = name
        self.optional = False
    def __repr__( self ):
        return self.name
        
# Food is an Item.
class Food( Item ):    
    pass
    
class Container( Item ):
    # Implement the __init__() method. Make sure that it allows for
    # the possibility to store items in this container.
    def __init__( self, name="", capacity=0 ):
        super().__init__( name )
    # Implement the __contains__() method, which is called when you
    # use the "in" operator. It returns True or False, namely True
    # if "item" is stored in this container, or in one of 
    # the containers which are stored in this container, or in 
    # one of the containers stored in the containers in this 
    # container, etc. Otherwise it returns False.
    def __contains__( self, item ):
        return False
    # Implement the store() method. This method stores "item" in
    # this container, if there is still enough capacity in this 
    # container. Return True if it succeeds, and False if you cannot 
    # store it.
    # OPTIONAL CHALLENGE: if "item" is a container, then make sure
    # that you are not trying to store it in itself. Also make sure
    # that this container is not itself stored somewhere in "item".
    # I.e., make sure that no "loops" are created.
    def store( self, item ):
        return False
    # Implement the __repr__() method. Make sure that it prints the
    # item's name, followed by, between parentheses, the capacity of
    # the container and the contents of the container (if you do this
    # correctly, it will not only show the contents of the container,
    # but also the contents of all the containers stored in the 
    # container, etc.).
    def __repr__( self ):
        return ""
        
# Bag is a Container.
class Bag( Container ):
    pass
    
def main():
    bigbag = Container( "big bag", 4 )
    apple = Food( "apple" )
    banana = Food( "banana" )
    bread = Food( "bread" )
    carrot = Food( "carrot" )
    mango = Food( "mango" )
    orange = Food( "orange" )
    
    bigbag.store( apple )
    bigbag.store( banana )
    bigbag.store( bread )
    bigbag.store( carrot )
    bigbag.store( orange ) # Does not fit!
    print( bigbag )
    
    bigbag = Container( "big bag", 4 ) # Create a new, empty big bag
    mediumbag = Container( "medium bag", 3 )

    mediumbag.store( apple )
    bigbag.store( banana )
    bigbag.store( mediumbag )
    bigbag.store( carrot )
    print( bigbag )

    smallbag = Container( "small bag", 2 )
    tinybag = Container( "tiny bag", 1 )
    smallbag.store( orange )
    mediumbag.store( smallbag )
    mediumbag.store( tinybag )
    tinybag.store( mango )
    print( bigbag )
    
    if bread in bigbag:
        print( "Big bag contains bread" )
    else:
        print( "Big bag does not contain bread" )
    if orange in bigbag:
        print( "Big bag contains an orange" )
    else:
        print( "Big bag does not contain an orange" )

    # Optional for those who want to take on an extra challenge
    if smallbag.optional:
        if smallbag.store( smallbag ):
            print( "You stored a bag in itself!" )
        else:
            print( "You did not allow a bag to be stored in itself." )
        if smallbag.store( bigbag ):
            print( "You allowed a bag to be stored in a bag which contains itself!" )
        else:
            print( "You did not allow a bag to be stored in a bag which contains itself." )
    else:
        print( "You did not implement the optional checks." )
    
'''
Correct output:

big bag(4, [apple, banana, bread, carrot])
big bag(4, [banana, medium bag(3, [apple]), carrot])
big bag(4, [banana, medium bag(3, [apple, small bag(2, [orange]), tiny bag(1, [mango])]), carrot])
Big bag does not contain bread
Big bag contains an orange
You did not implement the optional checks.

For the optional challenge, the last line is replaced by:

You did not allow a bag to be stored in itself.
You did not allow a bag to be stored in a bag which contains itself.

'''
    
if __name__ == "__main__":
    main()