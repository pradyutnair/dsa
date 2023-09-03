# Name:
# Student number:

'''
Take an integer, and add up the squares of its digits. This gives a new integer. 
Repeat the procedure with the new integer, and continue repeating the procedure 
until one of two things happens: (1) you end up at 1, or (2) you end up at an 
integer that you already had before. If you end up at 1, the integer you started 
with is "happy." Otherwise, it is "sad." Integers 0 and lower are "sad" by 
definition.

Write a function happy() which takes one argument, namely an integer. The function 
determines whether the argument is "happy." If it is, the function returns True, 
otherwise False.
'''

def happy( num ):
    return False
    
def main():
    print( happy( 0 ) )     # False
    print( happy( 1 ) )     # True
    print( happy( 2 ) )     # False
    print( happy( 7 ) )     # True
    print( happy( 18 ) )    # False
    print( happy( 19 ) )    # True
    print( happy( 108 ) )   # False
    print( happy( 109 ) )   # True
    print( happy( 1111 ) )  # False
    print( happy( 1112 ) )  # True
    print( happy( 123455 ) )# False
    print( happy( 123456 ) )# True
    
if __name__ == "__main__":
    main()