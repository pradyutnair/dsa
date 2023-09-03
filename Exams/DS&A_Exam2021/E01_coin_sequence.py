# Name:
# Student number:

from random import randint

# The function simulate() takes 3 arguments: n, k, and nsim.
# The argument n specifies the number of coin flips, the argument k 
# specifies the length of the sequence of identical flips, and the 
# argument nsim specifies the number of simulation to run. The function 
# should return the probability of a sequence of k identical flips 
# in a row in a series of n coin flips, as estimated through nsim 
# simulations of n coin flips.

def coin_flip():
    """
    Returns heads or tails encoded as 0 or 1
    :return: 0 or 1
    """
    return randint(0, 1)

def tracker(seq: list) -> int:
    """
    Finds the longest length of an indetical flip in a a sequence of flips
    :return: longest length of consecutive 0s or 1s in a sequence
    """
    length = 1
    new_length = 1
    for index in range(len(seq)-1):
        if seq[index] == seq[index+1]:
            new_length += 1
        else:
            new_length = 1
        if new_length > length:
            length = new_length
    return length


def simulate( n, k, nsim ):
    overall = 0
    # Conduct the simulations
    for _ in range(nsim):
        # Flip n coins
        flips = [coin_flip() for _ in range(n)]
        # Check if there is a sequence of k identical flips
        if tracker(flips) >= k:
            overall += 1
    # Return the probability of a sequence of k identical flips
    return round(overall/nsim, 3)

    
def main():
    print( "{:.3f}".format( simulate( 3, 2, 10000 ) ) ) # approximately 0.750
    print( "{:.3f}".format( simulate( 5, 3, 10000 ) ) ) # approximately 0.500
    print( "{:.3f}".format( simulate( 4, 3, 10000 ) ) ) # approximately 0.375
    print( "{:.3f}".format( simulate( 10, 4, 10000 ) ) ) # approximately 0.465

if __name__ == "__main__":
    main()
