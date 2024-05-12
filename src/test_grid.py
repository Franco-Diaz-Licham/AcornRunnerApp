from grid import grid_to_string
from player import Player
from game_parser import parse

# test positive test case, the first element of grid should be the player. 
def test_grid_1(parse):
    lines = ["*X*", "*1*", "*1*", "*Y*"]
    player = Player()
    grid_1 = parse(lines)
    actual_string = grid_to_string(grid_1,player)
    expected_string = "*A*\n*1*\n*1*\n*Y*\n\nYou have 0 water buckets."
    assert actual_string == expected_string, "Test failed"
    print("Test case 1: Grid Handled correctly!")

# test whether it prints out the number of water buckets.
def test_grid_2(parse):
    lines = ["*X*", "*1*", "*1*", "*Y*"]
    grid_1 = parse(lines)
    player = Player()
    player.num_water_buckets = 1
    grid_1 = parse(lines)
    actual_string = grid_to_string(grid_1,player)
    expected_string = "*A*\n*1*\n*1*\n*Y*\n\nYou have 1 water bucket."
    assert actual_string == expected_string, "Test failed"
    print("Test case 2: Grid Handled correctly!")

# test whether it prints if water buckets are 2.
def test_grid_3(parse):
    lines = ["*X*", "*1*", "*1*", "*Y*"]
    grid_1 = parse(lines)
    player = Player()
    player.num_water_buckets = 2
    grid_1 = parse(lines)
    actual_string = grid_to_string(grid_1,player)
    expected_string = "*A*\n*1*\n*1*\n*Y*\n\nYou have 2 water buckets."
    assert actual_string == expected_string, "Test failed"
    print("Test case 3: Grid Handled correctly!")

def run_tests():
    test_grid_1(parse)
    test_grid_2(parse)
    test_grid_3(parse)
    pass



