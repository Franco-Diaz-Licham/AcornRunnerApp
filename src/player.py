class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0
        self.move_count = 0
        self.at_the_start = True
        self.out_of_bounds = False
        self.running_to_wall = False
        self.maximum_row_value = 0
        self.maximum_col_value = 0

    def move(self, move):
        """updates the player's position and some of its attributes
        Arguments:
            move -- are the movement's of the user s,w,d,a,e
        Returns:
            self -- returns itself as the updated object
        """
        # attribute to allow us to draw the player where X is before any move we make.
        self.at_the_start = False

        # Return the same position of the player as we will be updating it based on the mechanism of the cell, in cells.py
        if move == "e":
            self.move_count += 1

        # move forward, update the row of the player +1, and the move count +1
        if move == "s":
            self.row += 1
            if self.row > self.maximum_row_value:
                self.row -= 1
                self.out_of_bounds = True
            self.move_count += 1
        
        # move back, update the row of the player -1, and the move count +1
        if move == "w":
            self.row -= 1
            # check if row is negative which means it wil be out of bounds
            # revert back previous row value.
            if self.row < 0:
                self.row += 1
                self.out_of_bounds = True
            self.move_count += 1
        
        # move right, update the row of the player +1, and the move count +1
        if move == "d":
            self.col += 1
            if self.col > self.maximum_col_value:
                self.row -= 1
                self.out_of_bounds = True
            self.move_count += 1

        # move left, update the row of the player -11, and the move count +1
        if move == "a":
            self.col -= 1 
            if self.col > self.maximum_col_value:
                self.row += 1
                self.out_of_bounds = True
            self.move_count += 1
        return self
    