# Name:
# Student number:

'''
Write a function remove_comments() which gets two string parameters: the name of an 
input file and the name of an output file. The function reads the contents of the 
input file, removes all the comments from the contents, and writes the adapted 
contents to the output file. It returns the number of characters written to the 
output file. If the input file does not exist, the function returns -1. You do not 
need to check for any other file errors.
The start of a comment is marked with the two-character combination "/*" (forward 
slash followed by asterisk). The end of the comment is marked by the first occurrence 
of the two-character combination "*/" after the start of the comment. The start and 
end of the comment are considered to be part of the comment, so when you remove a 
comment, they have to be removed as well.
A few remarks:
*	Comments may stretch over multiple lines of a file. 
*	There may be more than one comment in a file. 
*	There is no overlap between the start and end of a comment, so the combination 
    "/*/" is not the start and end of a comment, but the combination "/**/" is the 
    start and end of a comment.
*	If you find the start of a comment which is never followed by the end of a 
    comment, or the end of a comment which is not preceded by the start of a comment, 
    then those are not comments.
*	Comments are never "nested," so you only need to search for the first occurrence 
    of the end of a comment after the start of a comment and not take into account 
    what is actually in the comment.
'''

from os.path import isfile

def remove_comments( infile, outfile ):
    return -1
    
def main():
    print( remove_comments( "infile1.txt", "outfile1.txt" ) ) # 13
    print( remove_comments( "infile2.txt", "outfile2.txt" ) ) # 883
    print( remove_comments( "infile3.txt", "outfile3.txt" ) ) # 110
    print( remove_comments( "infile4.txt", "outfile4.txt" ) ) # 0
    print( remove_comments( "infile5.txt", "outfile5.txt" ) ) # 121
    print( remove_comments( "doesnotexist.txt", "willnotbecreated.txt" ) ) # -1
    
if __name__ == "__main__":
    main()