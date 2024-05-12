def print_moves(moves, game):
    """prints all the moves by the player.
    Arguments:
        game -- game object
    Returns:
        None
    """
    i = 0
    message = ''
    while i < len(moves):
        # check if player has not run into wall, count moves
        if game.player.running_to_wall == False:
            if i < len(moves) - 1:
                message = message + " " + str(moves[i]) + ','
            else:
                message = message + " " + str(moves[i])
        i += 1
    # check whether the player has made 1 move or moves, and print message accordingly.
    if len(moves) == 1:
        print("You made {} move.".format(game.player.move_count))
        print("Your move:{}".format(message))
    else:
        print("You made {} moves.".format(game.player.move_count))
        print("Your moves:{}".format(message))
    pass

def print_won_game(moves, game):
    """prints all the win message
    Arguments:
        game -- game object
    Returns:
        None
    """
    print()
    message_if_won = 'You conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.'
    print()
    print(message_if_won)
    print()
    print_moves(moves,game)
    print()
    print('=====================\n====== YOU WIN! =====\n=====================')
    pass

def print_lost_game(moves, game):
    """prints the loss message
    Arguments:
        game -- game object
    Returns:
        None
    """
    print()
    print()
    message_if_lost = 'You step into the fires and watch your dreams disappear :(.\n\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.'
    print(message_if_lost)
    print()
    print_moves(moves,game)
    print()
    print('=====================\n===== GAME OVER =====\n=====================')
    pass

def print_if_not_allowed_movement(game):
    """ print message if player is not allowed to move.
    Arguments:
        game -- game object
    Returns:
        None
    """
    # check if player ran into a wall
    if game.player.running_to_wall == True:
        print()
        print("You walked into a wall. Oof!")
        game.player.move_count -= 1
        game.player.running_to_wall = False
    
    # check if player is trying to go out of bounds
    if game.player.out_of_bounds == True:
        print()
        print("You walked into a wall. Oof!")
        game.player.move_count -= 1
        game.player.out_of_bounds = False
    pass

def print_if_water_found(game):
    """prints message if the player finds a water bucket.
    Arguments:
        game -- game object
    Returns:
        None
    """
    # check if player found water bucket.
    if game.found_water_bucket == True:
        print()
        print("Thank the Honourable Furious Forest, you've found a bucket of water!")
        game.found_water_bucket = False
    pass

def print_if_fire_out(game):
    """prints message if player puts fire out.
    Arguments:
        game -- game object
    Returns:
        None
    """
    # check if player has put fire out.
    if game.fire_out == True:
        print()
        print("With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")
        game.fire_out = False
    pass

def print_if_teleported(game):
    """prints message if player teleports.
    Arguments:
        game -- game object
    Returns:
        None
    """
    # check if player has been teleported.
    if game.teleportation == True:
        print()
        print("Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.")
        game.teleportation = False
    pass

def common_check(game,ch,moves):
    """prints messages based on the moves of the player.
    Arguments:
        game -- game object
        ch -- the input from the user w,a,s,d,e
        moves -- the list of moves to be printed.
    Returns:
        None
    """
    # if the input is w, a, d or s, they will all have the same checks to be conducted including
    # check whether movement is allowed, if water was found, if fire was put out or if we have teleported.
    game.game_move(ch)
    if game.player.running_to_wall == True:
        pass
    else:
        moves.append(ch)
    print(game.print)
    print_if_not_allowed_movement(game)
    print_if_water_found(game)
    print_if_fire_out(game)
    print_if_teleported(game)
    pass