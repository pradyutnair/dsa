# Name:
# Student number:

'''
The function same_letters() gets two parameters: a string word, and a list of strings wordlist. 
The function creates an output list of those words in wordlist which contain the same letters 
as word, and returns that output list. Words in the output list should remain in the same order 
as they were in wordlist. 
"Containing the same letters" means that the output list contains those words which contain 
each letter in word at least once, and no letters that are not in word.
The letters do not have to occur the same number of times. For instance, if word is "barber" 
and the word "bear" is in wordlist, then "bear" goes in the output list, even though it only 
contains one "b" and one "r" while "barber" contains two of each. The same also holds in the 
reverse order: if word is "bear" and "barber" is in wordlist, then "barber" goes in the output 
list, even though it contains the "b" and "r" twice, while "bear" only contains them once. 
You may assume that all the words consist of lower-case letters of the alphabet only.
'''

def same_letters( word, wordlist ):
    return []
    
def main():
    print( same_letters( "bear",   [ "bare", "beer", "barber", "bar", "bears" ] ) )
    # ['bare', 'barber']
    print( same_letters( "barber", [ "bare", "beer", "bear", "bar", "bears" ] ) )
    # ['bare', 'bear']
    print( same_letters( "hearth", [ "earth", "heart", "there", "theater", "theaters" ] ) ) 
    # ['earth', 'heart', 'theater']
    print( same_letters( "berry",  [ "strawberry", "grape", "banana", "raspberry" ] ) )
    # []
    print( same_letters( "grape",  [ "pear", "banana", "raspberry" ] ) )
    # []
    print( same_letters( "least",  [ "latest", "last", "stale", "stalest", "slate", "stalls", "pastel" ] ) )
    # ['latest', 'stale', 'stalest', 'slate']
    
if __name__ == "__main__":
    main()