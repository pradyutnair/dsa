# Name:
# Student number:

'''
The exercise file contains a class Citizen, which has a name and an age.  This class is already complete.
There is also a class City, which has a name.  A city may house multiple citizens, which are added to the city using the method add_citizen(). The method average_age() calculates the average age over all citizens in the city. It returns -1 if there are no citizens in a city. You should create reasonable implementations for the methods __init__(), add_citizen(), average_age(), and __repr__().      
Finally, there is a class Country, which has a name.  A country may have multiple cities, which are added to the country using the method add_city(). The method average_age() calculates the average age over all citizens in the country. It returns -1 if there are no citizens in a country. You should create reasonable implementations for the methods __init__(), add_city(), average_age(), and __repr__().      
'''

class Citizen():
    def __init__( self, name, age ):
        self.name = name
        self.age = age
    def __repr__( self ):
        return f"Citizen({self.name},{self.age})"
        
class City():
    def __init__( self, name ):
        pass
    def add_citizen( self, citizen ):
        pass
    def average_age( self ):
        return -1
    def __repr__( self ):
        return ""
        
class Country():
    def __init__( self, name ):
        pass
    def add_city( self, city ):
        pass
    def average_age( self ):
        return -1
    def __repr__( self ):
        return ""
        
def main():
    tilburg = City( "Tilburg" )
    print( tilburg.average_age() ) # -1

    tilburg.add_citizen( Citizen( "Bob", 25 ) )
    tilburg.add_citizen( Citizen( "Mary", 31 ) )
    tilburg.add_citizen( Citizen( "Joseph", 16 ) )
    tilburg.add_citizen( Citizen( "Julie", 29 ) )
    print( tilburg.average_age() ) # 25.25

    denbosch = City( "Den Bosch" )
    denbosch.add_citizen( Citizen( "Albert", 45 ) )
    denbosch.add_citizen( Citizen( "Bruce", 51 ) )
    denbosch.add_citizen( Citizen( "Samantha", 32 ) )
    denbosch.add_citizen( Citizen( "Henry", 48 ) )
    denbosch.add_citizen( Citizen( "Erica", 42 ) )
    denbosch.add_citizen( Citizen( "Sandy", 46 ) )
    print( denbosch.average_age() ) # 44.0

    netherlands = Country( "The Netherlands" )
    netherlands.add_city( tilburg )
    netherlands.add_city( denbosch )
    print( netherlands.average_age() ) # 36.5

if __name__ == "__main__":
    main()