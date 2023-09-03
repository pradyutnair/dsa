# Name:
# Student number:

'''
Armstrong numbers are numbers the digits of which, when cubed and summed, are equal to the number itself.
For example, the number 153 has the digits 1, 5, and 3; 1**3 + 5**3 + 3**3 = 153, which means that 153 
is an Armstrong number. Note: 0 and 1 are also Armstrong numbers.
Write a function armstrong_range() which takes two arguments, start and finish, which specify the lower 
and upper bound of a range of integers. Both start and finish are 0 or greater, and finish is greater 
than or equal to start. The function checks whether each number in the range, starting from start and 
ending with finish, is an Armstrong number.
The function returns a list of all Armstrong numbers in the range provided.
'''

def armstrong_range( start, finish ):
    return []

def main():
    print( armstrong_range( 0, 1000 ) ) # [0, 1, 153, 370, 371, 407]
    print(armstrong_range( 0, 100 ) )   # [0, 1]
    print( armstrong_range( 100, 370 ) )# [153, 370]
    print( armstrong_range( 50, 100 ) ) # []
    print( armstrong_range( 407, 407 ) )# [407]
    print( armstrong_range( 0, 153 ) )  # [0, 1, 153]

if __name__ == "__main__":
    main()
