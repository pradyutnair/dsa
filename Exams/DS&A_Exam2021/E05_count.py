# Name:
# Student number:

# Determine the time complexity of the following five functions. Each
# function determines how often the letter "letter" occurs in string "s".
# Assume that the length of the string s is n. Write your answers as
# comments below each of the functions. Also explain your answers briefly.
# An answer without an explanation is wrong!

# You may assume the following:
# The function len() is O(1)
# The function int() is O(1)
# The function list() is O(n), where n is the length of the object turned into a list
# The list method remove() is O(n), where n is the length of the list
# The string method split() is O(n), where n is the length of the string
# The string method join() is O(n), where n is the length of the list that is joined
# Taking a substring from a string is O(n), where n is the length of the substring


# count1 processes each letter of the string, adding 1 to a count if it is the
# sought letter.
def count1( s, letter ):
    total = 0
    for char in s:
        if char == letter:
            total += 1
    return total
# Time complexity of count1():
# --- Write your answer here.


# count2 initializes a count to the length of the string, then subtracts 1 from the 
# count each time it finds a letter which should not be counted.
def count2( s, letter ):
    total = len( s )
    for char in s:
        if char != letter:
            total -= 1
    return total
# Time complexity of count2():
# --- Write your answer here.

    
# count3 turns the string into a list, then counts how often the sought letter can
# be removed from the list.
def count3( s, letter ):
    total = 0
    lists = list( s )
    while letter in lists:
        lists.remove( letter )
        total += 1
    return total
# Time complexity of count3():
# --- Write your answer here.

    
# count4 splits the string on the letter, then joins it again. By comparing the
# length of the string before the operation with the length of the string after
# the operation, the count can be determined.
def count4( s, letter ):
    lists = s.split( letter )
    news = "".join( lists )
    return len( s ) - len( news )
# Time complexity of count4():
# --- Write your answer here.

        
# count5 recursively divides the string in two, until it needs to deal with a
# string of a single letter. If that letter is the sought letter, it returns 1,
# otherwise zero. By adding up the results of each recursive call, the total
# count is determined.
def count5( s, letter ):
    if len( s ) <= 1:
        if s == letter:
            return 1
        return 0
    mid = int( len( s )/2 )
    return count5( s[:mid], letter ) + count5( s[mid:], letter )
# Time complexity of count5():
# --- Write your answer here.

    
def main():
    s = "The rain in Spain falls mainly on the plain."
    print( count1( s, "n" ) )
    print( count2( s, "n" ) )
    print( count3( s, "n" ) )
    print( count4( s, "n" ) )
    print( count5( s, "n" ) )
    
if __name__ == "__main__":
    main()
