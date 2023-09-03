# Name:
# Student number:

from math import sqrt

class Shape:
    def __init__( self, name="" ):
        self.name = type( self ).__name__
        if len( name ) > 0:
            self.name = name
    def circumference( self ):
        return NotImplemented
    def __repr__( self ):
        return self.name

class Point:
    def __init__( self, x, y ):
        self.x = x
        self.y = y
    def distance( self, p ):
        return sqrt( (self.x - p.x)**2 + (self.y - p.y)**2 )
    def __repr__( self ):
        return "({},{})".format( self.x, self.y )

# Create a Polygon which inherits from Shape and implements
# the __init__(), circumference(), and __repr__() methods.
# Keep the parameters for __init__() as given.
class Polygon:
    def __init__( self, vertices ):
        pass
    def circumference( self ):
        return 0
    
# Create a Rectangle which inherits from Polygon and ONLY 
# implements the __init__() method.
# Keep the parameters for __init__() as given.
class Rectangle:
    def __init__( self, point, width, height ):
        pass
    def circumference( self ):
        return 0

# Create a Square which inherits from Rectangle and ONLY 
# implements the __init__() method.
# Keep the parameters for __init__() as given.
class Square:
    def __init__( self, point, side ):
        pass
    def circumference( self ):
        return 0
    
def main():
    p1 = Polygon( [Point(1,3), Point(-3,4), Point(-3,0), \
        Point(4,-2), Point(5,-1), Point(2,4)] )
    print( p1, p1.circumference() )
    p2 = Polygon( [Point(0,0), Point(3,4), Point(3,0)] )
    print( p2, p2.circumference() )
    r = Rectangle( Point(2,2), 3, 1 )
    print( r, r.circumference() )
    s = Square( Point(-1,1), 2 )
    print( s, s.circumference() )
    '''
The output for these calls should be:

Polygon([(1,3), (-3,4), (-3,0), (4,-2), (5,-1), (2,4)]) 24.062594534489673
Polygon([(0,0), (3,4), (3,0)]) 12.0
Rectangle([(2,2), (5,2), (5,1), (2,1)]) 8.0
Square([(-1,1), (1,1), (1,-1), (-1,-1)]) 8.0
    '''
    
if __name__ == "__main__":
    main()