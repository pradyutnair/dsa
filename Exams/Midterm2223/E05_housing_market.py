# Name:
# Student number:

'''
The template file for the exercise contains a class Location and a class Property. A location has a name and a square-meter price. A property has a name, a size, and a location. The price of a property is calculated by multiplying the size by the square-meter price of the location. E.g., a property of size 100 with a square-meter price of 1000, costs 100,000. These two classes have already been implemented according to the given specifications. This calculation is done by a method price().
Three classes inherit from Property: Apartment, House, and Castle. You must implement these three classes. In particular, you have to ensure that the price() method for each of these classes calculates the correct price. Make sure that you implement the correct inheritance relationships! 
An Apartment is a Property and behaves just like the general property.
A House is a Property. However, a house also has a garden, of which the size is specified when the house is created (i.e., the size of the garden is an extra, fourth parameter given to the __init__() method). To calculate the price of a house, to the size is added one-fourth of the size of the garden. E.g., if the size of a house is 100 and there is a garden of size 50, with a square-meter price of 1000, the price is 112,500. For the class House, you have to implement the methods __init__(), price(), and __repr__().    
A Castle is a House. As it may be difficult to find a buyer for a castle, the price of a castle is lowered for every day that it is for sale. Therefore, to the price() method of a castle an extra parameter is given, namely the number of days-for-sale. Lower the price of the castle by 0.02% for every day that it is for sale, with a maximum of 1000 days for sale (after 1000 days, the price is not lowered further). This entails that you multiply the calculated price by (1-days_for_sale*0.0002). For the class Castle, you have to implement the method price().
'''

class Location:
    def __init__( self, name, price ):
        self.name = name
        self.price = price
    def __repr__( self ):
        return f"Location({self.name},{self.price})"

class Property:
    def __init__( self, name, size, location ):
        self.name = name
        self.size = size
        self.location = location
    def price( self ):
        return self.size * self.location.price
    def __repr__( self ):
        return f"{self.__class__.__name__}({self.name},{self.size},{self.location})"

class Apartment():
    pass

class House():
    pass

class Castle():
    pass

if __name__ == '__main__':
    loc_upper = Location( "Upper class", 4000 )
    loc_average = Location( "Average", 3200 )
    loc_lower = Location( "Lower class", 2500 )
    '''
    high_rise_245 = Apartment( "High Rise 245", 80, loc_lower )
    print( f"{high_rise_245.name}: ${high_rise_245.price()}" )
    high_rise_188 = Apartment( "High Rise 188", 85, loc_lower )
    print( f"{high_rise_188.name}: ${high_rise_188.price()}" )
    
    fifth_street_15 = House( "5th Street 15", 95, loc_average, 70 )
    print( f"{fifth_street_15.name}: ${fifth_street_15.price()}" )
    snooty_lane_1 = House( "Snooty Lane 1", 134, loc_upper, 220 )
    print( f"{snooty_lane_1.name}: ${snooty_lane_1.price()}" )
    
    chivalric_towers = Castle( "Chivalric Towers", 742, loc_upper, 1270 )
    print( f"{chivalric_towers.name}: ${chivalric_towers.price(0)}" )
    print( f"{chivalric_towers.name}: ${chivalric_towers.price(500)}" )
    print( f"{chivalric_towers.name}: ${chivalric_towers.price(1000)}" )
    print( f"{chivalric_towers.name}: ${chivalric_towers.price(2000)}" )
    '''
    print( "Done." )
    
# Output for tests:
# High Rise 245: $200000
# High Rise 188: $212500
# 5th Street 15: $360000
# Snooty Lane 1: $756000
# Chivalric Towers: $4238000
# Chivalric Towers: $3814200
# Chivalric Towers: $3390400
# Chivalric Towers: $3390400