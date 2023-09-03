# Name:
# Student number:

'''
The function compare_files() gets two parameters, both of which are names of files. These files contain integers, one integer per line. They contain nothing else. You may assume that each file contains at least one number. The numbers in the files can appear in any order.
The function determines the fraction of the integers in the second file which are higher than all the integers in the first file. I.e., suppose that the highest integer in the first file is 50, and there are 100 integers in the second file, of which 75 are 51 or higher, then the requested fraction is 0.75. The function returns this fraction.
In case one or both of the file names are of files which do not exist, then the function returns -1. You do not need to check for any other file errors.
'''

from os.path import isfile

def compare_files( file1, file2 ):
    return -1
    
def main():
    print( compare_files( "numbers1.txt", "numbers2.txt" ) ) # 0.4
    print( compare_files( "numbers1.txt", "numbers3.txt" ) ) # 0.7
    print( compare_files( "numbers1.txt", "numbers4.txt" ) ) # 0.8
    print( compare_files( "numbers1.txt", "numbers5.txt" ) ) # 0.75
    print( compare_files( "numbers1.txt", "numbers6.txt" ) ) # 0.8
    print( compare_files( "numbers2.txt", "numbers1.txt" ) ) # 0.0
    print( compare_files( "numbers3.txt", "numbers4.txt" ) ) # 0.1
    print( compare_files( "numbers4.txt", "numbers3.txt" ) ) # 0.0
    print( compare_files( "numbers5.txt", "numbers6.txt" ) ) # 0.8
    print( compare_files( "numbers6.txt", "numbers5.txt" ) ) # 0.0
    print( compare_files( "numbers1.txt", "numbers5.txt" ) ) # 0.75
    print( compare_files( "numbers5.txt", "numbers1.txt" ) ) # 0.0

if __name__ == "__main__":
    main()