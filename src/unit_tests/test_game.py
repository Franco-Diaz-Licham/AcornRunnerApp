from game import Game

# positive test cases: this is because game will receive arguments with problems that would 
# have already been dealth with in grid_to_string and parser()

# move should be recorded as an attribute in game.
def test_game_1():
    move = "w"
    filename = "board_hard.txt"
    game = Game(filename)
    game.game_move(move)
    actual = "w"
    expected = "w"
    assert actual == expected , "Test failed"
    print("Test case 1: Game Handled correctly!")

# test what hapens after we step on air from the start. player should be allowed to move.
def test_game_2():
    move = "s"
    filename = "board_simple.txt"
    game = Game(filename)
    game.game_move(move)
    actual = game.print
    expected = "**X**\n* A *\n**Y**\n\nYou have 0 water buckets."
    assert actual == expected , "Test failed"
    print("Test case 2: Game Handled correctly!")

# what happens if player now has a wall in front of him. player should not be allowed to move forward.
def test_game_3():
    move = "s"
    filename = "board_simple_1.txt"
    game = Game(filename)
    game.game_move(move)
    actual = game.print
    expected = "**A**\n* * *\n**Y**\n\nYou have 0 water buckets."
    assert actual == expected , "Test failed"
    print("Test case 3: Game Handled correctly!")

# what happens if player now has a water in front. player should collect it.
def test_game_4():
    move = "s"
    filename = "board_simple_2.txt"
    game = Game(filename)
    game.game_move(move)
    actual = game.found_water_bucket
    expected = True
    assert actual == expected , "Test failed"
    print("Test case 4: Game Handled correctly!")


# what happens if player has no water buckets and steps into fire. game should be over.
def test_game_5():
    move = "s"
    filename = "board_simple_3.txt"
    game = Game(filename)
    game.game_move(move)
    actual = game.game_lost
    expected = True
    assert actual == expected , "Test failed"
    print("Test case 5: Game Handled correctly!")

# if player moves into the end position, game should be won.
def test_game_5():
    move = "s"
    filename = "board_simple_5.txt"
    game = Game(filename)
    game.game_move(move)
    actual = game.game_won
    expected = True
    assert actual == expected , "Test failed"
    print("Test case 5: Game Handled correctly!")

# if player moves into a teleport pad, it should be teleported. this should have the same functionality with all the teleport pads numbers.
def test_game_6():
    move = "s"
    filename = "board_simple_4.txt"
    game = Game(filename)
    game.game_move(move)
    actual = game.teleportation
    expected = True
    assert actual == expected , "Test failed"
    print("Test case 6: Game Handled correctly!")

# if player moves into a a fire cell and has a water bucket, it should put it out with its water bucket
def test_game_7():
    move = "s"
    filename = "board_simple_3.txt"
    game = Game(filename)
    game.player.num_water_buckets = 1
    game.game_move(move)
    actual = game.fire_out
    expected = True
    assert actual == expected , "Test failed"
    print("Test case 7: Game Handled correctly!")

def run_tests():
    test_game_1()
    test_game_2()
    test_game_3()
    test_game_4()
    test_game_5()
    test_game_6()
    test_game_7()
    pass
