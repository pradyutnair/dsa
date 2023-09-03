# Name:
# Student Number:

'''
The template for this exercise contains a class Data. When a Data object is created, you give it a 
filename (string). The class has two methods which you need to create: parseFile()and search().  
You are allowed to make changes to the __init__() method, and to add extra methods.
parseFile() is called once, and pre-processes the file. It gets no parameters. It returns False 
if the file does not exist, otherwise it returns True. The preprocessing should make sure that 
you can search the file contents for words, consisting of letters from the alphabet. The letters 
can be upper-case or lower-case, and the search should be case-sensitive (so distinguish between 
upper-case and lower-case). The parseFile() method should have a time complexity which is at worst 
O(n*log(n)), with n being the number of separate words that can be found in the file.
After parseFile() has been called, you can search for words (which only consist of letters from the 
alphabet). You do this with the search() method. This method gets the target (string) that you are 
searching for as parameter. It returns True if the target can be found, and otherwise False. The 
search should be at worst O(log(n)), with n being the number of separate words that can be found 
in the file. 
'''

from os.path import isfile

class Data:
    def __init__( self, filename ):
        self.filename = filename

    def parseFile( self ):
        fp = open( self.filename, encoding="utf-16" )
        fp.close()
        return False

    def search( self, target ):
        return False

def main():
    myData = Data( "transcripts.txt" )
    if myData.parseFile():
        print ( myData.search( "sdafa" ) )      # False
        print ( myData.search( "illuminati" ) ) # True
        print ( myData.search( "Masters" ) )    # False
        print ( myData.search( "masters" ) )    # True
        print ( myData.search( "CIA" ) )        # True
        print ( myData.search( "IAC" ) )        # False

if __name__ == "__main__":
    main()