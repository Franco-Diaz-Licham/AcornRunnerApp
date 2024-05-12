from auxiliary_teleport_functions import (finding_teleport, update_player_position, step_movement)

class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        """updates the state of the game
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        return game.grid

class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        """updates the state of the game if reaches to the end
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        game.game_won = True
        return game.grid

class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        """updates the state of the game if the next cell is air
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        return game.grid

class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        """updates the state of the game based if the cell is a wall
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        # update the state of the player that he is running into a wall
        game.player.running_to_wall = True

        if game.player.running_to_wall == True:
            pass
        else:
            player.move_count += 1
        
        # update the position of the player because He is not allowed to step of a cell that is a wall
        if game.move == "s":
            game.player.row -= 1
        if game.move == "w":
            game.player.row += 1
        if game.move == "d":
            game.player.col -= 1
        if game.move == "a":
            game.player.col += 1
        return game.grid

class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        """updates the state of the game based if the cell is a fire
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        # check if the player has a water bucket and put the fire out if we have water, otherwise we loose the game.
        if game.player.num_water_buckets > 0:
            game.grid[game.player.row][game.player.col] = Air()
            game.player.num_water_buckets -= 1
            game.fire_out = True
        else:
            game.game_lost = True
        return game.grid
        pass

class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        """updates the state of the game
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        # collect the water and move forward.
        game.player.num_water_buckets += 1
        game.grid[game.player.row][game.player.col] = Air()
        game.found_water_bucket = True
        return game.grid

class Teleport:
    def __init__(self,display):
        self.display = display

    def step(self, game):
        """calls step_movement() which is a series of functions to update the position of player
        Arguments:
            game -- game object to access grid
        Returns:
            grid -- the new upgraded grid
        """
        step_movement(game,self.display)
        return game.grid