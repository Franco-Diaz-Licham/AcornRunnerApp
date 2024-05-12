# import all the import functions and modules required.
from game_parser import read_lines, parse
from grid import grid_to_string
from player import Player

class Game:
    def __init__(self, filename):
        # create attributes for the player and grid objects, the string of the 
        # game to be printed, the states whether we have lost or won the game, 
        # found a water bucket have put out a fire or have been teleported. 
        self.player = Player()
        self.grid = parse(read_lines(filename))
        self.print = grid_to_string(self.grid,self.player)
        self.move = None
        self.game_won = False
        self.game_lost = False
        self.found_water_bucket = False
        self.fire_out = False
        self.teleportation = False
    
    def game_move(self, move):
        """updates the player's position and the state of the grid
        Arguments:
            move -- are the movement's of the user s,w,d,a,e
        Returns:
            None
        """
        # make the player move
        self.player = self.player.move(move)

        # make attribue move in game so that cells.py can access what type of 
        # movement the player is making
        self.move = move
        
        # make variables row and col to keep track of the players position 
        # and cell to varify what tyep of cell is the player stepping on
        row = self.player.row
        col = self.player.col
        cell = self.grid[row][col]

        # make the player move and the respective behaviour based on the type of cell.
        self.grid = cell.step(self)

        # update the game to be printed in run with the updated 
        # grid and the player objects.
        self.print = grid_to_string(self.grid,self.player)
        pass