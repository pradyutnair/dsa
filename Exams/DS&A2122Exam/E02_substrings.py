# Name:
# Student number:

'''
The function find_superstring()gets one parameter: a list which contains strings. 
These strings only contain letters of the alphabet, and are all lower-case. 
Some of the strings in the list are substrings of other strings in the list. 
Your goal is to find the "superstring," which is the string which has most of the 
other strings in the list as substrings. The function should return the "superstring." 
If there is more than one string which has the most substrings, then return the one 
earliest in the alphabet. You are allowed to change the list in the function.
'''

def find_superstring( slist ):
    return ""
    
def main():
    slist = ["broth","brother","chemotherapy","her",
        "moth","mother","other","rot","smother","the"] 
    print( find_superstring( slist ) ) #brother
    slist = ["and","ant","boar","board","broth","brother",
        "brotherhood","chemotherapy",
        "grand","grandmother","her","herb",
        "hip","his","hood","man","moth","mother",
        "motherboard","oar","odd","other","random",
        "rot","ship","sword","swordsmanship","the",
        "therapy","woman","word"]
    print( find_superstring( slist ) ) # motherboard
    
if __name__ == "__main__":
    main()