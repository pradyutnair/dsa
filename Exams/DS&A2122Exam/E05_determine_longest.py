# Name:
# Student number:

'''
Each of the functions, which are all named determine_longest_x(), gets one parameter: slist which 
is a list of strings. The function returns the longest string in the list (if there are multiple, 
it will return one of them). For each of the functions, write as a comment in the file what the 
time complexity is (immediately below the function), and give a brief explanation on how you 
determined this. If you do not add an explanation, the answer is automatically considered to be 
wrong. In your big-O notation of the time complexity, you may use n to refer to the length of the 
list. You may assume the following:
* Taking a sublist from a list is O(n), where n is the length of the sublist
* The list method sort() is O(n*log(n)), where n is the length of the list
* The statement del list[i] is  O(n), where n is the length of the list
'''

# Processes each string in the list, keeping track of the longest.
def determine_longest_1( slist ):
    longest = ""
    for s in slist:
        if len( s ) > len( longest ):
            longest = s
    return longest

# Sorts the list by length, then returns the last element.
def determine_longest_2( slist ):
    if len( slist ) < 1:
        return ""
    slist.sort( key=len )
    return slist[-1]

# Compares the first two elements of the list and removes the shortest, 
# until only one element remains.
def determine_longest_3( slist ):
    if len( slist ) < 1:
        return ""
    copylist = slist[:]
    while len( copylist ) > 1:
        if len( copylist[0] ) > len( copylist[1] ):
            del copylist[1]
        else:
            del copylist[0]
    return copylist[0]

# Compares the first element of the list with the longest element of the 
# rest of the list. The longest element of the rest of the list is determined 
# by a recursive call to the function itself with the rest of the list 
# as parameter.
def determine_longest_4( slist ):
    if len( slist ) < 1:
        return ""
    s = determine_longest_4( slist[1:] )
    if len( slist[0] ) > len( s ):
        return slist[0]
    return s

# Splits the list in two, and recursively calls itself with the two sublists. 
# It determines the longest string that is returned from those two calls. 
# If it gets called with a list with only one element, it returns that element.
def determine_longest_5( slist ):
    if len( slist ) < 1:
        return ""
    elif len( slist ) == 1:
        return slist[0]
    i = len( slist )//2
    s1 = determine_longest_5( slist[:i] )
    s2 = determine_longest_5( slist[i:] )
    if len( s1 ) > len( s2 ):
        return s1
    return s2

def main():
    namelist = ["apple", "pear", "banana", "orange", "grapefruit", "kiwi"]
    print( determine_longest_1( namelist ) )
    print( determine_longest_2( namelist ) )
    print( determine_longest_3( namelist ) )
    print( determine_longest_4( namelist ) )
    print( determine_longest_5( namelist ) )

if __name__ == "__main__":
    main()