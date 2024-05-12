def finding_teleport(game, num_teleport):
    """finds location of teleport cells from game.grid.
    Arguments:
        game -- game object to access grid
        num_teleport -- the teleport pad number, 1 to 9
    Returns:
        tel_locations -- contains a string with the positions of the teleport pads
    """
    tel_locations = []
    i = 0
    while i < len(game.grid):
        j = 0
        while j < len(game.grid[i]):
            ch = game.grid[i][j].display
            if ch == num_teleport:
                tel_locations.append([i,j])
            j += 1
        i += 1
    return tel_locations


def update_player_position(game,tel_locations):
    """upadtes the location of player based on the teleport number
    Arguments:
        game -- game object to access grid
        num_teleport -- the teleport pad number, 1 to 9
    Returns:
        None
    """
    location_1 = tel_locations[0]
    location_2 = tel_locations[1]
    # check whether player is at location 1 of the teleport pad
    if [game.player.row,game.player.col] == location_1:
        game.player.row = location_2[0]
        game.player.col = location_2[1]
    # check whether player is at location 2 of the teleport pad
    elif [game.player.row,game.player.col] == location_2:
        game.player.row = location_1[0]
        game.player.col = location_1[1]
    pass

def step_movement(game,display):
    """calls both the finding_teleport() and update_player_position() to update the state of the game
    Arguments:
        game -- game object to access grid
        num_teleport -- the teleport pad number, 1 to 9
    Returns:
        None
    """
    tel_locations = finding_teleport(game, display)
    update_player_position(game, tel_locations)
    game.teleportation = True
    pass