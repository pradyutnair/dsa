# Name:
# Student number:

'''
The function sum_and_product() gets two parameters, which are both integers valued 0 or higher. You should find three integers, which, when added up, produce the first of the two parameters, and when multiplied with each other produce the second of the two parameters.
For instance, if the first parameter is 15 and the second is 105, then three integers which produce these are 3, 5, and 7, because 3+5+7=15 and 3*5*7=105. 
You return the three integers as a tuple, where the three integers are ordered from low to high. In the example above, you return (3, 5, 7). 
If no solution can be found, you return (-1, -1, -1).
'''

def sum_and_product( isum, iproduct ):
    return -1, -1, -1
    
def main():
    print( sum_and_product( 3+5+7, 3*5*7 ) )     # (3,5,7)
    print( sum_and_product( 99, 33*33*33 ) )     # (33,33,33)
    print( sum_and_product( 100, 33*33*34 ) )    # (33,33,34)
    print( sum_and_product( 100, 7038 ) )        # (3,46,51)
    print( sum_and_product( 100, 98 ) )          # (1,1,98)
    print( sum_and_product( 100, 194 ) )         # (1,2,97)
    print( sum_and_product( 3, 1 ) )             # (1,1,1)
    print( sum_and_product( 4, 2 ) )             # (1,1,2)
    print( sum_and_product( 0, 0 ) )             # (0,0,0)
    print( sum_and_product( 2, 0 ) )             # (0,0,2) or (0, 1, 1)
    print( sum_and_product( 2, 1 ) )             # (-1,-1,-1)
    print( sum_and_product( 3, 2 ) )             # (-1,-1,-1)
    print( sum_and_product( 100, 2000 ) )        # (-1,-1,-1)
    
if __name__ == "__main__":
    main()