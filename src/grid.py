def grid_to_string(grid, player):
    """prints the grid and the player as a string
        Arguments:
            grid -- object of the grid
            player -- object of the player
        Returns:
            string_1 -- contains the grid and player as a string
    """
    # string_1 will contain all the information as a string
    string_1 = ''

    # go through the grid list of list of cells
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            # define ch to make checking a bit easier to read
            ch = grid[i][j].display

            # if this is at the start of the play, make sure to place the player where X is.
            # Otherwise, if we have already moved, place the player according to its movement
            if player.at_the_start == True and ch == "X":
                ch = player.display
                player.row = i
                player.col = j
            elif player.at_the_start == False and [player.row, player.col] == [i,j]:
                ch = player.display
            
            # concatinate the strings into string_1 and update the values of j and i
            string_1 = string_1 + ch
            j += 1
        string_1 += "\n"
        i += 1
    
    # take advantage of this function to set the maximum value for the player's row and col so
    # we do not go out of bounds
    player.maximum_row_value = i
    player.maximum_col_value = j

    # return the number of buckets that the player has as a string
    if player.num_water_buckets == 0:   
        string_1 = string_1 + '\n' + 'You have 0 water buckets.'
    elif player.num_water_buckets == 1:   
        string_1 = string_1 + '\n' + 'You have 1 water bucket.'
    else:
        string_1 = string_1 + '\n' + 'You have {} water buckets.'.format(player.num_water_buckets)
    
    # return the list of list of cells and the player as a string to be printed
    return string_1