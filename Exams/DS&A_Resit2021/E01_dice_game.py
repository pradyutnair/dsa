# Name:
# Student number:

from random import randint

# The function dice_game_simulation() takes 3 arguments: ndice1, ndice2, and nsim.
# The argument ndice1 specifies the number of dice thrown by player 1, whereas the 
# argument ndice2 specifies the number of dice thrown by player 2. The 
# argument nsim specifies the number of simulations to run. The player with 
# the highest total wins the game. In case of a tie, both players throw their 
# dice again. The function should return the probability of player 1 winning 
# the game, as estimated through nsim simulations of the dice throwing game.


def simulate_dice_game( ndice, ndice_opp, nsim ):
    beat = 0
    for _ in range(nsim):
        # Player 1
        player1 = [randint(1, 6) for _ in range(ndice)]
        # Player 2
        player2 = [randint(1, 6) for _ in range(ndice_opp)]
        # Check if player 1 wins
        if sum(player1) > sum(player2):
            beat += 1
        # Check if there is a tie
        elif sum(player1) == sum(player2):
            # Player 1
            player1 = [randint(1, 6) for _ in range(ndice)]
            # Player 2
            player2 = [randint(1, 6) for _ in range(ndice_opp)]
            # Check if player 1 wins
            if sum(player1) > sum(player2):
                beat += 1
    # Return the probability of player 1 winning
    return beat/nsim


    
def main():
    print( "{:.3f}".format( simulate_dice_game( 2, 2, 10000 ) ) ) # approximately .500
    print( "{:.3f}".format( simulate_dice_game( 3, 2, 10000 ) ) ) # approximately .837
    print( "{:.3f}".format( simulate_dice_game( 2, 3, 10000 ) ) ) # approximately .163
    print( "{:.3f}".format ( simulate_dice_game( 5, 4, 10000 ) ) ) # approximately .765

if __name__ == "__main__":
    main()
