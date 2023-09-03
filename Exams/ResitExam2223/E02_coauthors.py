# Name:
# Student number:

# In this exercise, you need to build a dictionary of authors of scientific papers and their coauthors.
# You need to implement the function build_coauthors_dictionary().
# That function gets one parameter, which is the name of a file.
# Files contain, on each line, and separated by commas: title, several names of authors, and number of citations.
# You need to build a dictionary of authors and their coauthors.
# The keys are the author names, and the values are lists of coauthors in alphabetical order.

from os.path import isfile


def build_coauthor_dictionary( filename ):
    return {}


def main():
    for filename in ["papers1.txt","papers2.txt","doesnotexist.txt"]:
        authors_dict = build_coauthor_dictionary( filename )
        if authors_dict == {}:
            print( "Not a papers-file\n" )
            continue
        keylist = list( authors_dict.keys() )
        keylist.sort()
        for author in keylist:
            s = ", ".join( authors_dict[author] )
            print( f"{author}: {s}" )
        print()

if __name__ == "__main__":
    main()