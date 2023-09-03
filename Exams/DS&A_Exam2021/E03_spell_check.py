# Name:
# Student number:

from os.path import isfile

# Correct_spelling takes two arguments, sentence (string) and dictfile (string, 
# which is a filename). Replace the words in sentence that are in the spelling error 
# dictionary dictfile. Return the corrected sentence. Return -1 if dictfile does not 
# exist.
def correct_spelling( sentence, dictfile ):
    # Write your code here
    return ""
    
def main():
    infile = "wikipedia.txt"
    sentences = [
      "I recomend the aplication of a progrom that corrects each and eveyr mispelling",
      "I am disatisfied with tghe perfromance of tihs algoritm",
      "Perhaps a omre comphrehensive dtictionary fo spleling erros owudl alliviate tje \
       probelm",
      "Or maybe better approachs exist"
    ]
    for sentence in sentences:
        print( correct_spelling( sentence, infile ) )
    # Output: 
    # I recommend the application of a program that corrects each and every misspelling
    # I am dissatisfied with the perfromance of this algorithm
    # Perhaps a more comprehensive dtictionary fo spleling erros would alleviate the 
    # problem
    # Or maybe better approaches exist

if __name__ == "__main__":
    main()