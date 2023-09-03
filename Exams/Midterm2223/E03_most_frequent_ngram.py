# Name:
# Student number:

'''
An N-gram is a sequence of N letters. For instance, "ABA" is a 3-gram, while "ABABC" is a 5-gram. You can investigate N-grams which occur in a string. For instance, in the string "ABABC" there are three different 2-grams, namely: "AB", "BA", and "BC". The 2-gram "AB" occurs twice, as you can see. The string "AAAAA" contains only one 2-gram, namely "AA", which occurs four times.
Write a function most_frequent_ngram() which gets two parameters: a string which is a sequence of letters, and a positive integer which indicates a length. The function should return the N-gram of the specified length which occurs the most in the string. If there are multiple candidates which occur the most, you may return any of them (though in the test examples provided there is always only one answer). You may assume that the length specified is at least 1 and at most the length of the string.
A possible approach (though not the only approach) for this exercise is to build a dictionary where the N-grams are the keys and the values are the corresponding counts.
'''

def most_frequent_ngram( letters, length ):
    return ""
    
def main():
    print( most_frequent_ngram( "AABBB", 1 ) ) # B
    print( most_frequent_ngram( "AABBB", 2 ) ) # BB
    print( most_frequent_ngram( "AABBB", 5 ) ) # AABBB
    print( most_frequent_ngram( "BABCAAABCBCACBCCABCCBAABCABABCABCA", 1 ) ) # A
    print( most_frequent_ngram( "BABCAAABCBCACBCCABCCBAABCABABCABCA", 2 ) ) # BC
    print( most_frequent_ngram( "BABCAAABCBCACBCCABCCBAABCABABCABCA", 3 ) ) # ABC
    print( most_frequent_ngram( "AXYXXYYYXXXAXXXYYXYZYYXAZXYYXYXY", 1 ) )   # X
    print( most_frequent_ngram( "AXYXXYYYXXXAXXXYYXYZYYXAZXYYXYXY", 2 ) )   # XY
    print( most_frequent_ngram( "AXYXXYYYXXXAXXXYYXYZYYXAZXYYXYXY", 3 ) )   # YYX
    print( most_frequent_ngram( "AXYXXYYYXXXAXXXYYXYZYYXAZXYYXYXY", 5 ) )   # XYYXY
   
if __name__ == "__main__":
    main()