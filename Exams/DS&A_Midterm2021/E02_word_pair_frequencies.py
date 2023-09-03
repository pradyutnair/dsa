# Name:
# Student number:

# Clean the text s
def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

# Return a dictionary with word pairs (tuples) as keys and frequencies as values
def word_pair_frequencies( text ):
    return {}

def main():
    # This is the input text.
    # You need to calculate frequencies of word pairs in this text.
    eggs_and_ham = """
    I am Sam. Sam I am.

    That Sam-I-am!
    That Sam-I-am!
    I do not like that Sam-I-am!

    Do you like 
    green eggs and ham?
    I do not like them, Sam-I-am.
    I do not like
    green eggs and ham."""

    # Call the function for eggs_and_ham
    wp_frequencies = word_pair_frequencies( eggs_and_ham )
    
    print( wp_frequencies.get( ("sam", "i"), 0 ) )        # 5
    print( wp_frequencies.get( ("i", "am"), 0 ) )         # 6
    print( wp_frequencies.get( ("green", "eggs"), 0 ) )   # 2
    print( wp_frequencies.get( ("red", "eggs"), 0 ) )     # 0
    print( wp_frequencies.get( "green eggs", 0 ) )        # 0
    print( wp_frequencies.get( ("and", "ham"), 0 ) )      # 2

if __name__ == "__main__":
    main()
