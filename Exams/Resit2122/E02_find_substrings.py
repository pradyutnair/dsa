# Name:
# Student number:

'''
In this exercise you search the contents of a file for substrings in unique words 
and return how many there are.
The function gets two parameters: a file name and a target substring. The function
returns an integer that is the number of words in the file that contain the target,
without counting duplicate words multiple times. For example, if the target is 
"Blitz" and there are three instances of the word "Blitzkrieg" and one instance 
of "Blitzkreeg" in the file, then the integer returned should be 2 (assuming that
no other words in the file contain "Blitz"). 
You may assume that words only consist of letters of the alphabet, and that all 
other characters in the file are punctuation. I.e., "didn't" is considered to be 
two words, "didn" and "t". Handle the words in the file case-sensitively.
If the target is an empty string, since an empty string is a substring of any 
word, the function will return the total number of unique words in the file.
If the file does not exist, return -1. You do not need to handle any other file 
errors.
'''

from os.path import isfile

def find_substrings_in_file( file, target ):
    return -1

def main():
    print( find_substrings_in_file( "wikipedia.txt", "year" ) )      # 4
    print( find_substrings_in_file( "wikipedia.txt", "Year" ) )      # 0
    print( find_substrings_in_file( "wikipedia.txt", "ear" ) )       # 35
    print( find_substrings_in_file( "wikipedia.txt", "r" ) )         # 2056
    print( find_substrings_in_file( "wikipedia.txt", "R" ) )         # 4
    print( find_substrings_in_file( "wikipedia.txt", "recipient" ) ) # 2
    print( find_substrings_in_file( "jeeves7.txt", "zab" ) )         # 1
    print( find_substrings_in_file( "jeeves7.txt", "favor" ) )       # 0
    print( find_substrings_in_file( "jeeves7.txt", "our" ) )         # 11
    print( find_substrings_in_file( "jeeves7.txt", "" ) )            # 1251
    print( find_substrings_in_file( "doesnotexist.txt", "our" ) )    # -1

if __name__ == "__main__":
    main()
    