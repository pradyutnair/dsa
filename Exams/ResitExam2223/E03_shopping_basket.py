# Name:
# Student number:

# You need to add items to a shopping basket and calculate the final price of the whole basket
# You must implement the class Basket and the two item classes WeightedItem and UnitsItem, which inherit from Item.
# Objects of class WeightedItem have a name and price per kilogram.
# In WeightedItem, calculate_price() receives the amount in grams and will return the price of the total amount.
# Objects of UnitsItem have a name and the price per unit.
# In UnitsItem, calculate_price() receives as an argument the number of units and returns the price of the total amount.
# For the Basket class, you need to implement three methods: __init__(), add_item(), and create_receipt().
# With the add_item() method, objects of the classes WeightedItem and UnitsItem can be added to a Basket.
# The method receives an item and an amount corresponding to the kind of object.
# create_receipt() calculates the total price of all the items in the basket and returns a string.
# The string must contain lines with an item name, the total amount in the basket of such an Item, and the total price.


class Basket:
    
    def __init__( self ):
        pass

    def add_item( self, item, amount ):
        pass

    def create_receipt( self ):
        return "No receipt"


class Item:
    def __init__( self, name ):
        self.name = name

    def calculate_price( self, amount ):
        return 0

    def __repr__( self ):
        return f"{self.name}"


class WeightedItem( Item ):
    def __init__( self, name, price_per_kilo ):
        pass

    def calculate_price( self, grams ):
        return 0

    def __repr__( self ):
        return ""


class UnitsItem( Item ):
    def __init__( self, name, price_per_unit ):
        pass

    def calculate_price( self, units ):
        return 0

    def __repr__( self ):
        return ""


def main():
    basket = Basket()
    item_1 = WeightedItem( "Oats", 3.5 )
    item_2 = UnitsItem( "Bun", 0.7 )
    item_3 = UnitsItem( "Baguette", 1 )
    item_4 = WeightedItem( "Rice", 4 )

    basket.add_item( item_1, 500 )
    basket.add_item( item_2, 2 )
    basket.add_item( item_2, 3 )
    basket.add_item( item_3, 3 )
    basket.add_item( item_4, 1500 )
    
    print( basket.create_receipt() )
    
if __name__ == '__main__':
    main()
