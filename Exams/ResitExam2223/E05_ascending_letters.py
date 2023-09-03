# Name:
# Student number:

# For each of the functions, write as a comment in the file what the time complexity is 
# (immediately below the function), and give a brief explanation on how you determined this. 
# If you do not add an explanation, the answer is automatically considered to be wrong. 
# In your big-O notation of the time complexity, you may use n to refer to the length of the word.
# You may assume the following:
# * Making a copy of a string is O(n), where n is the length of the string
# * Casting a string to a list is O(n), where n is the length of the string
# * The range() iterator is O(1)
# * The function len() is O(1)
# * The list method sort() for a list of length n is O(n*log(n))
# * The string method join() with a list of length n as argument is O(n)

# ascending_1() compares every letter of the word to the next one.
def ascending_1( word ):
    for i in range( len( word )-1 ):
        if word[i] > word[i+1]:
            return False
    return True

# ascending_2() compares every letter of the word with all the letters in the part of the word 
# which comes after that letter.
def ascending_2( word ):
    for i in range( len( word )-1 ):
        for j in range( i, len( word ) ):
            if word[i] > word[j]:
                return False
    return True

# ascending_3() turns the word into a list, sorts the list, and then compares the sorted list with 
# the original list of letters.
def ascending_3( word ):
    word = list( word )
    sorted_word = word[:]
    sorted_word.sort()
    return word == sorted_word

# ascending_4() turns the word into a list, then compares each letter with the next and swaps them 
# if they are not in ascending order; after that it turns the new list into a string again and 
# compares it with the original word.
def ascending_4( word ):
    wordlist = list( word )
    for i in range( len( wordlist )-1 ):
        if wordlist[i] > wordlist[i+1]:
            wordlist[i], wordlist[i+1] = wordlist[i+1], wordlist[i]
    return "".join( wordlist ) == word

# ascending_5() recursively checks whether the first letter of a word is lower than the first letter 
# of the rest of the word, and if the rest of the word is also in ascending order.
def ascending_5( word ):
    if len( word ) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return ascending_5( word[1:] )

def main():
    print( ascending_1( "first" ) )
    print( ascending_1( "last" ) )
    print( ascending_2( "first" ) )
    print( ascending_2( "last" ) )
    print( ascending_3( "first" ) )
    print( ascending_3( "last" ) )
    print( ascending_4( "first" ) )
    print( ascending_4( "last" ) )
    print( ascending_5( "first" ) )
    print( ascending_5( "last" ) )

if __name__ == "__main__":
    main()

