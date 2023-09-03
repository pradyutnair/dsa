# Name:
# Student number:

'''
Each of the functions, which are all named reverse_x() (x being a number), 
gets one parameter: sentence which is a string. The function returns the 
reverse of this string.

For each of the functions, write as a comment in the file what the time 
complexity is (immediately below the function), and give a brief 
explanation on how you determined this. If you do not add an explanation, 
the answer is automatically considered to be wrong. In your big-O 
notation of the time complexity, you may use n to refer to the length 
of the string.

You may assume the following:
* Concatenating two strings, one of length m and one of length n, is O(m+n)
* Taking a substring of length n from a string is O(n)
* The iterator range() is O(1)
* The function len() is O(1)
* Using the list() function on a string of length n is O(n)
* The string method join() is O(n), where n is the length of the list argument
* The list method reverse() is O(n), where n is the length of the list
'''

# reverse_1() takes each letter of the string one by one and adds it 
# at the start of a new string.
def reverse_1( sentence ):
    newsentence = ""
    for c in sentence:
        newsentence = c + newsentence
    return newsentence

# reverse_2() processes the letters of the string by index from last 
# to first, and adds them to a new string.
def reverse_2( sentence ):
    newsentence = ""
    for i in range( len( sentence )-1, -1, -1 ):
        newsentence += sentence[i]
    return newsentence

# reverse_3() removes the last letter from the string and adds it to 
# a new string, continuing to do this until the original string is empty.
def reverse_3( sentence ):
    newsentence = ""
    while len( sentence ) > 0:
        newsentence += sentence[-1]
        sentence = sentence[:-1]
    return newsentence
    
# reverse_4() turns the string into a list, reverses the list, and then 
# joins the list to become a new string.
def reverse_4( sentence ):
    listsentence = list( sentence )
    listsentence.reverse()
    return "".join( listsentence )

# reverse_5() recursively splits the string into the first letter and 
# the rest of the string, and then adds the first letter to the end of 
# what the recursive call returns.
def reverse_5( sentence ):
    if len( sentence ) <= 1:
        return sentence
    return reverse_5( sentence[1:] ) + sentence[0]
    
def main():
    print( reverse_1( "carbonhydroxide" ) )
    print( reverse_2( "carbonhydroxide" ) )
    print( reverse_3( "carbonhydroxide" ) )
    print( reverse_4( "carbonhydroxide" ) )
    print( reverse_5( "carbonhydroxide" ) )
    
if __name__ == '__main__':
    main()