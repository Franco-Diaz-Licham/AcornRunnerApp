from game_parser import parse

# testing positive tests
def test_parse_1(parse):
    
    # testing 1
    lines = ["*X*", "* *", "*Y*"]
    grid = parse(lines)
    expected = "*"
    actual = grid[0][0].display
    assert actual == expected, "Test case failed"
    print("Test case 1: Parser handled correctly!")

def test_parse_2(parse):
    
    # test positive test case, the first element of grid should be 
    lines = ["*X*", "*1*", "*1*", "*Y*"]
    grid = parse(lines)
    i = 0
    actual_pad_number = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].display == "1":
                actual_pad_number += 1
            j += 1
        i += 1
    expected_pad_number = 2
    assert actual_pad_number == expected_pad_number, "Test failed"
    print("Test case 2: Parser handled correctly!")
#
#
#
# testing negative test cases:
def test_parse_3(parse):
    lines = ["*Xb", "* *", "*Y*"]
    expected = ValueError("Bad letter in configuration file: b.")
    fail_message = "Test case 3: bad letter mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 3: Parser handled correctly!")
    except Exception:
        print(fail_message)

def test_parse_3(parse):
    lines = ["*XX", "* *", "*Y*"]
    expected = ValueError("Expected 1 starting position, got 2.")
    fail_message = "Test case 3: too many starting positions mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 3: Parser handled correctly!")
    except Exception:
        print(fail_message)

def test_parse_4(parse):
    lines = ["***", "* *", "*Y*"]
    expected = ValueError("Expected 1 starting position, got 0.")
    fail_message = "Test case 4: not enough starting positions mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 4: Parser handled correctly!")
    except Exception:
        print(fail_message)

def test_parse_5(parse):
    lines = ["*X*", "* *", "*YY"]
    expected = ValueError("Expected 1 ending position, got 2.")
    fail_message = "Test case 5: too many ending positions mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 5: Parser handled correctly!")
    except Exception:
        print(fail_message)

def test_parse_6(parse):
    lines = ["*X*", "* *", "***"]
    expected = ValueError("Expected 1 ending position, got 0.")
    fail_message = "Test case 6: not enough ending positions mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 6: Parser handled correctly!")
    except Exception:
        print(fail_message)

def test_parse_7(parse):
    lines = ["*X*", "*1*", "*Y*"]
    expected = ValueError("Teleport pad 1 does not have an exclusively matching pad.")
    fail_message = "Test case 7: teleport pad mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 7: Parser handled correctly!")
    except Exception:
        print(fail_message)
#
#
#
#
# testing edge cases: empty list, proving a list of strings and numbers
def test_parse_8(parse):
    
    lines = []
    expected = ValueError("The list is empty")
    fail_message = "Test case 8: Mishandled :("
    try:
        actual = parse(lines)
    except ValueError as e:
        assert str(expected) == str(e), fail_message
        print("Test case 8: Parser handled correctly!")
    except Exception:
        print(fail_message)

def run_tests():
    test_parse_1(parse)
    test_parse_2(parse)
    test_parse_3(parse)
    test_parse_4(parse)
    test_parse_5(parse)
    test_parse_6(parse)
    test_parse_7(parse)
    test_parse_8(parse)
    pass
