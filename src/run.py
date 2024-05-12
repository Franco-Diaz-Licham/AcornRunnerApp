# import all the import functions and modules required.
from game import Game
import os
import sys
from auxiliary_printing_functions import (print_if_not_allowed_movement, print_won_game, 
print_lost_game, print_if_water_found, print_if_fire_out, print_if_teleported, common_check)

if len(sys.argv) == 1:
    # receive the command line argument as filename to open
    print("Usage: python3 run.py <filename> [play]")
    sys.exit()
else:
    filename = sys.argv[1]

# create a game object and print the game at the start
directory = "<directory>"
filepath = directory + filename
game = Game(filepath)
print(game.print)

# create a list called "moves" which will keep track of the 
# moves made to be printed.
moves = []

try:
    # keep the game running
    while True:
        
        # check whether we have lost or won the game print all the correct 
        # messages and exit the game.
        if game.game_lost == True:
            print_lost_game(moves,game)
            break
        if game.game_won == True:
            print_won_game(moves,game)
            break

        # receive the input from the user and clear the cmd
        print()
        ch = input("Input a move: ").lower()

        os.system("clear")

        # check the user input, ask for another input if it is wrong
        if ch not in ["q", "e", "w", "a", "d", "s"]:
            print(game.print)
            print()
            print("Please enter a valid move (w, a, s, d, e, q).")
            

        # if the input from the user is "q", print "bye" and exit the game
        if ch == "q":
            print()
            print("Bye!")
            break

        # if the input is "e" print the correct message for teleportation
        elif ch == "e":
            game.game_move(ch)
            print(game.print)
            moves.append(ch)
            print_if_teleported(game)
        
        # input values of w, a, d or s, will share common operations.
        elif ch == 'w':
            common_check(game,ch,moves)
        elif ch == "a":
            common_check(game,ch,moves)
        elif ch == "d":
            common_check(game,ch,moves)
        elif ch == "s":
            common_check(game,ch,moves)

# handle any exception raised in other modules.
except ValueError as e:
    print(e)
    sys.exit()
