"""
A simple program that will import your tests and run them all!
Be sure you include tests for your other modules like cells and player!

Usage: python3 test_all.py
"""

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_player import run_tests as test_player

# testing parser, grid, player and game would be the most important modules to test because they contain important functions.
# parser is very important when reading on the configuration files and hence would encouter most positive, negative an edge cases.
# the game_parser module would also be dealing with most of the exceptions can be be risen like FileNotFound, etc... grid_to_string, 
# is constantly printing, so it is important to test this. Player would be making changes to the state of the player so 
# it is important to test the method. game is dependent upon the functionality of cells.py. Hence in testing game, we would be 
# testing the mechanisms that the cells conduct on the game, and thus cells have been left out from unit testing. run.py has been 
# excluded from testing also because it will only be passing information between the user and game.py and printing the state 
# of the game. Most of the testing for run.py is included in the e2e testing since we will be testing what is printed on the 
# screen of the user.

print()
print("#############################")
print("# Running unit parse tests! #")
print("#############################\n")

test_parser()

print("\n############################")
print("# Running unit grid tests! #")
print("############################\n")

test_grid()

print("\n############################")
print("# Running unit player tests! #")
print("#############################\n")

test_player()

print("\n###########################")
print("# Running unit game tests! #")
print("############################\n")

test_game()
print()

# Run the e2e script
subprocess.call(['./test_e2e.sh'])
