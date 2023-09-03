# Name:
# Student number:

# A perfect number is a number that is equal to the sum of its proper divisors (i.e., all
# the numbers that divide it without leaving a remainder, except for the number itself).
# The function perfect returns true if its parameter is a perfect number.

def perfect( num ):
    pass

def main():
    for i in range( 1, 10000 ):
        if perfect( i ):
            print( i )
            
if __name__ == "__main__":
    main()