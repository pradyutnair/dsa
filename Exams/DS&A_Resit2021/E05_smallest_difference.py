# Name:
# Student number:

# Determine the time complexity of the following five functions. Each
# function gets a list of numbers, and returns the smallest difference
# between any of the two numbers on the list. The assumption is that there
# are at least two numbers in the list (the functions do not check for
# that). Assume that the length of the list numlist is n. 
# Write your answers as comments below each of the functions. Also explain 
# your answers briefly. An answer without an explanation is wrong!

# You may assume the following:
# The function abs() is O(1)
# The function len() is O(1)
# The function max() is O(n), where n is the length of the sequence from which you take the maximum
# The function min() is O(n), where n is the length of the sequence from which you take the minimum
# The iterator range() is O(1)
# The list method append() is O(1)
# The list method remove() is O(n), where n is the length of the list
# The list method sort() is O(n*log(n)), where n is the length of the list
# Taking a sublist from a list is O(n), where n is the length of the sublist

# smallestdiff1. For each element of the list, the function checks the difference between the
# element and all the remaining elements of the list, keeping track of the smallest.
def smallestdiff1( numlist ):
    sdiff = abs( numlist[1] - numlist[0] )
    for i in range( len( numlist ) ):
        for j in range( i+1, len( numlist ) ):
            if abs( numlist[i] - numlist[j] ) < sdiff:
                sdiff = abs( numlist[i] - numlist[j] )
    return sdiff
# --- Write your answer for smallestdiff1 here:

# smallestdiff2. The function first sorts the list, then calculates for each element the difference
# with the next element on the list, keeping track of the smallest.
def smallestdiff2( numlist ):
    listcopy = numlist[:]
    listcopy.sort()
    sdiff = listcopy[1] - listcopy[0]
    for i in range( 2, len( listcopy ) ):
        if listcopy[i] - listcopy[i-1] < sdiff:
            sdiff = listcopy[i] - listcopy[i-1]
    return sdiff
# --- Write your answer for smallestdiff2 here:
    
# smallestdiff3. First the list is copied. Then, in a loop, the difference between the two 
# largest elements of the list is determined, whereby the very largest is removed. This
# continues until the list has only one element left. The smallest difference is tracked.
def smallestdiff3( numlist ):
    sdiff = abs( numlist[1] - numlist[0] )
    listcopy = numlist[:]
    biggest = max( listcopy )
    while len( listcopy ) > 1:
        listcopy.remove( biggest )
        m = max( listcopy )
        if biggest - m < sdiff:
            sdiff = biggest - m
        biggest = m
    return sdiff
# --- Write your answer for smallestdiff3 here:
    
# smallestdiff4. A new list is built which contains all the differences between all pairs of
# elements of the original list. This new list is sorted, and the smallest difference (which is
# then at the start of the list) is returned.
def smallestdiff4( numlist ):
    difflist = []
    for i in range( len( numlist ) ):
        for j in range( i+1, len( numlist ) ):
            difflist.append( abs( numlist[i] - numlist[j] ) )
    difflist.sort()
    return difflist[0]
# --- Write your answer for smallestdiff4 here:
        
# smallestdiff5. This is a recursive implementation. If the list has only two elements, then
# the difference is returned. Otherwise, the list is sorted, the difference between the first
# two elements is determined, and the smallest difference for the list without the first 
# element is determined. Of these two differences, the smallest is returned.
def smallestdiff5( numlist ):
    if len( numlist ) <= 2:
        return abs( numlist[0] - numlist[1] )
    listcopy = numlist[:]
    listcopy.sort()
    sdiff = listcopy[1] - listcopy[0]
    sdiffrest = smallestdiff5( listcopy[1:] )
    return min( sdiff, sdiffrest )
# --- Write your answer for smallestdiff5 here:
    
def main():
    numlist = [ 20, -8, 77, -215, 53, 107, 5 ]
    print( smallestdiff1( numlist ) )
    print( smallestdiff2( numlist ) )
    print( smallestdiff3( numlist ) )
    print( smallestdiff4( numlist ) )
    print( smallestdiff5( numlist ) )
    
if __name__ == "__main__":
    main()
