# Name:
# Student number:

'''
Each of the functions, which are all named smallest_plus_largest_x() (x being a number), 
gets one parameter: numlist which is a list of numbers (the length of the list is at 
least 1). The function returns the sum of the smallest and the largest number on the list.
For each of the functions, write as a comment in the file what the time complexity is 
(immediately below the function), and give a brief explanation on how you determined this. 
If you do not add an explanation, the answer is automatically considered to be wrong. 
In your big-O notation of the time complexity, you may use n to refer to the length of 
the list.

You may assume the following:
* Taking a sublist from a list is O(n), where n is the number of items in the sublist.
* The iterator range() is O(1).
* The function len() is O(1).
* The function min() is O(n), where n is the number of items given to the function.
* The function max() is O(n), where n is the number of items given to the function.
* The method sort) is O(n*log(n)), where n is the length of the list that is sorted.
'''

# Just take the minimum and maximum of numlist and return the sum.
def smallest_plus_largest_1( numlist ):
    return min( numlist ) + max( numlist )
    
# Go through numlist, remembering the values for the smallest and
# largest, then return the sum.
def smallest_plus_largest_2( numlist ):
    smallest = numlist[0]
    largest = numlist[0]
    for i in numlist:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return smallest + largest
    
# Same as the previous one, except that the function now remembers 
# the indices of the smallest and largest.
def smallest_plus_largest_3( numlist ):
    smallest = 0
    largest = 0
    for i in range( 1, len( numlist ) ):
        if numlist[i] < numlist[smallest]:
            smallest = i
        if numlist[i] > numlist[largest]:
            largest = i
    return numlist[smallest] + numlist[largest]
    
# Sort the list, then return the sum of the first and last number.
def smallest_plus_largest_4( numlist ):
    copylist = numlist[:]
    copylist.sort()
    return copylist[0] + copylist[-1]

# This function uses a recursive implementation of functions that
# find the smallest and largest numbers. The recursive implementations
# split the list in two, find the smallest (or largest) on each of
# the sublists, then return the smallest (or largest) of them.
def smallest_plus_largest_5( numlist ):
    def smallest( numlist ):
        if len( numlist ) <= 1:
            return numlist[0]
        mid = len( numlist )//2
        return min( smallest( numlist[:mid] ), smallest( numlist[mid:] ) )
    def largest( numlist ):
        if len( numlist ) <= 1:
            return numlist[0]
        mid = len( numlist )//2
        return max( largest( numlist[:mid] ), largest( numlist[mid:] ) )
    return smallest( numlist ) + largest( numlist )

def main():
    numlist = [8,19,3,22,7,-5,4,0,17,5,5,12]
    print( smallest_plus_largest_1( numlist ) )
    print( smallest_plus_largest_2( numlist ) )
    print( smallest_plus_largest_3( numlist ) )
    print( smallest_plus_largest_4( numlist ) )
    print( smallest_plus_largest_5( numlist ) )
    
if __name__ == "__main__":
    main()
    
    
    