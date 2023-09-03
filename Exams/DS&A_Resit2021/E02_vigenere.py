# Name:
# SNR:

# Encode the sentence with a Vigenere cipher using the codeword.
# Basically, each letter in the codeword indicates a distance, whereby
# A=0, B=1, C=2, etc. For each letter between A and Z in the sentence, 
# add the corresponding distance in the codeword to it, decoding it to 
# a new letter. The "corresponding distance" for a letter at index i
# is the distance in the codeword at position i%len(codeword). Return
# the encoded sentence. You may assume that both the sentence and the
# codeword have only upper-case letters, and that the codeword has
# nothing but letters.
def vigenere( sentence, codeword ):
    return ""


def main():
    print( vigenere( "CATCATCAT", "DOG" ) )
    print( vigenere( "ATTACKATDAWN", "LEMON" ) )
    print( vigenere( "PPHMPZWHPNLJ", "LEMON" ) )
    print( vigenere( "PKTS YMYNRE RB UK XOAN. EW HJB JADDEM FV EP. " + \
        "RF DDD NGBPNHO JWP CRYE CA IHPT RFZ PLKNA!", "EXPARROT" ) )
'''
FOZFOZFOZ
LXFOPVEFRNHR
ATTACKATDAWN
THIS PARROT IS NO MORE. IT HAS CEASED TO BE. IT HAS EXPIRED AND GONE TO MEET ITS MAKER!
'''
    
if __name__ == "__main__":
    main()