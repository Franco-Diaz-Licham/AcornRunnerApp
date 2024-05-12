from player import Player

# positive test cases: this is because player will receive arguments with problems that would 
# have already been dealth with in grid_to_string and parser()

def test_player_1():
    move = "w"
    player = Player()
    player.row = 2
    expected = 1
    player.move(move) 
    actual = player.move_count
    assert actual == expected, "Test failed"
    print("Test case 1: Player handled correctly!")

# test what "s" would do. it should move the player forward.
def test_player_2():
    move = "s"
    player = Player()
    expected = 1
    player.move(move) 
    actual = player.move_count
    assert actual == expected, "Test failed"
    print("Test case 2: Player handled correctly!")

# test what "d" would do. should move the player to the right
def test_player_3():
    move = "d"
    player = Player()
    expected = 1
    player.move(move) 
    actual = player.move_count
    assert actual == expected, "Test failed"
    print("Test case 3: Player handled correctly!")

# test what "a" would do. should move the player to the left.
def test_player_4():
    move = "a"
    player = Player()
    expected = 1
    player.move(move) 
    actual = player.move_count
    assert actual == expected, "Test failed"
    print("Test case 4: Player handled correctly!")

# test what "e" would do. count it as a move.
def test_player_5():
    move = "e"
    player = Player()
    player.col = 2
    expected = 1
    player.move(move) 
    actual = player.move_count
    assert actual == expected, "Test failed"
    print("Test case 5: Player handled correctly!")

# similar test will run for all the other conditions if out of bounds. player should not be allowed to move.
def test_player_6():
    player = Player()
    move = "s"
    player.maximum_row_value = 4
    player.row = 5
    player.move(move)
    expected = True
    actual = player.out_of_bounds
    assert actual == expected, "Test failed"
    print("Test case 6: Player handled correctly!")

def run_tests():
    test_player_1()
    test_player_2()
    test_player_3()
    test_player_4()
    test_player_5()
    test_player_6()
    pass
