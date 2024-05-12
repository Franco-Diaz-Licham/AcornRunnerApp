# import all the import functions and modules required.
from cells import (Start,End,Air,Wall,Fire,Water,
    Teleport)
import sys

def read_lines(filename):
    """Transform the txt input into a list of strings.
    Arguments:
        filename -- txt input
    Returns:
        lines -- list of strings
    """
    try:
        file = open(filename,"r")
        lines = []
        while True:
            line = file.readline().strip()
            if line == "":
                break
            lines.append(line)
        file.close()
        return lines
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        sys.exit()


def parse(lines):
    """Transform the input into a grid.
    Arguments:
        lines -- list of strings representing the grid
    Returns:
        list -- contains list of lists of Cells
    """
    if len(lines) == 0:
        raise ValueError("The list is empty")

    # create all objects necessary given in cells.py
    start = Start()
    end = End()
    air = Air()
    fire = Fire()
    water = Water()
    wall = Wall()
    teleport_1 = Teleport("1")
    teleport_2 = Teleport("2")
    teleport_3 = Teleport("3")
    teleport_4 = Teleport("4")
    teleport_5 = Teleport("5")
    teleport_6 = Teleport("6")
    teleport_7 = Teleport("7")
    teleport_8 = Teleport("8")
    teleport_9 = Teleport("9")
    
    # create variables which will keep track whether any teleport pad from 0 to 9 come in pairs
    count_teleport_1 = 0
    count_teleport_2 = 0
    count_teleport_3 = 0
    count_teleport_4 = 0
    count_teleport_5 = 0
    count_teleport_6 = 0
    count_teleport_7 = 0
    count_teleport_8 = 0
    count_teleport_9 = 0

    # create variable count_x to keep track of the starting position and variable coun
    count_x = 0
    count_y = 0

    # grid will the list of list of cell objects returned to be stored as an object in game.py
    grid = []

    # go through every element list from read_lines()
    i = 0
    while i < len(lines):
        list_1 = []
        j = 0
        while j < len(lines[i]):
            # create variable ch so that it makes it easier to read
            ch = lines[i][j]

            # convert element ch to its appropriate object. e.g. if ch is a wall, then convert string to an object
            # Update any variables such as count_x, count_y, and count_teleport_1, etc... in order to raise any exceptions.
            if ch == "*":
                list_1.append(wall)
            elif ch == "Y":
                list_1.append(end)
                count_y += 1
            elif ch == "X":
                list_1.append(start)
                count_x += 1
            elif ch == ' ':
                list_1.append(air)
            elif ch == "F":
                list_1.append(fire)
            elif ch == "W":
                list_1.append(water)
            elif ch == "1":
                list_1.append(teleport_1)
                count_teleport_1 += 1
            elif ch == "2":
                list_1.append(teleport_2)
                count_teleport_2 += 1
            elif ch == "3":
                list_1.append(teleport_3)
                count_teleport_3 += 1
            elif ch == "4":
                list_1.append(teleport_4)
                count_teleport_4 += 1
            elif ch == "5":
                list_1.append(teleport_5)
                count_teleport_5 += 1
            elif ch == "6":
                list_1.append(teleport_6)
                count_teleport_6 += 1
            elif ch == "7":
                list_1.append(teleport_7)
                count_teleport_7 += 1
            elif ch == "8":
                list_1.append(teleport_8)
                count_teleport_8 += 1
            elif ch == "9":
                list_1.append(teleport_9)
                count_teleport_9 += 1
            else:
                # raise an exception if we find a letter which 
                raise ValueError("Bad letter in configuration file: {}.".format(ch))
            j += 1
        grid.append(list_1)
        i += 1
    
    # create variable t to represent the allowed number of teleport pads which are either 0 or 2.
    t = [0,2]

    # check for how many starting and ending positions there are, and raise error accordingly.
    if count_x == 0:
        raise ValueError("Expected 1 starting position, got {}.".format(count_x))
    elif count_x >= 2:
        raise ValueError("Expected 1 starting position, got {}.".format(count_x))
    elif count_y >= 2: 
        raise ValueError("Expected 1 ending position, got {}.".format(count_y))
    elif count_y == 0:
        raise ValueError("Expected 1 ending position, got {}.".format(count_y))
    
    # check whether any teleport pad has no matching teleportation pad. Raise value error if there is no matching pafd
    elif count_teleport_1 not in t or count_teleport_2 not in t or count_teleport_3 not in t or count_teleport_4 not in t or \
    count_teleport_5 not in t or count_teleport_6 not in t or count_teleport_7 not in t or count_teleport_8 not in t or \
    count_teleport_9 not in t:
        string = [count_teleport_1, count_teleport_2, count_teleport_3, count_teleport_4, count_teleport_5, \
        count_teleport_6, count_teleport_7, count_teleport_8, count_teleport_9]
        i = 1
        pad_number = 0
        while i <= len(string):
            if string[i-1] == 1:
                pad_number = i
                pass
            i += 1
        raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pad_number))
    return grid