# Name:
# Student number:

# numlist is a list of numbers.
# Return true if the list contains two numbers (with different indices)
# whereby one is a divider of the other. Otherwise return False.
def contains_dividers( numlist ):
    if len(numlist) <= 1:
        return False
    for index in range(len(numlist)):
        for index2 in range(len(numlist)):
            if index != index2:
                if numlist[index] % numlist[index2] == 0:
                    return True
    return False
    
def main():
    print( contains_dividers( [7,6,5,4,3,29] ) )  # True
    print( contains_dividers( [7,6,5,4,29] ) )    # False
    print( contains_dividers( [] ) )              # False
    print( contains_dividers( [4] ) )             # False
    print( contains_dividers( [4,2] ) )           # True
    print( contains_dividers( [11,7,5,3,2] ) )    # False
    print( contains_dividers( [2,3,5,7,11] ) )    # False
    print( contains_dividers( [11,7,5,33,2] ) )   # True
    print( contains_dividers( [2,33,5,7,11] ) )   # True
    print( contains_dividers( [11,7,5,3,2,11] ) ) # True
    print( contains_dividers( [2,3,5,7,1] ) )     # True

if __name__ == "__main__":
    main()