# Name:
# Student number:

from os.path import isfile

# The function decode() takes two arguments, message (string) and keyfile (string, 
# which is a filename). Message is a message in Morse code that can be decoded using 
# the Morse code alphabet in keyfile. Characters are separated by spaces, words are 
# separated by forward slashes ("/"). Return the decoded message. 
# Return "" if keyfile does not exist.
def decode( message, keyfile ):
    # Write your code here
    return ""
    
def main():
    keyfile = "morsecode.txt"
    messages = [
      ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -..",
      "- .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. .",
      "-.-. .- -. / -.-- --- ..- / -.. . -.-. --- -.. . / .. - ..--.."
    ]

    for message in messages:
        print( decode( message, keyfile ) )
    # Output: 
    # HELLO, WORLD
    # THIS IS MORSE CODE
    # CAN YOU DECODE IT?

if __name__ == "__main__":
    main()
