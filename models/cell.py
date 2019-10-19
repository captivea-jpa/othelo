# DIRECTIONS is a list of direction to use to get the next cell from another one in that direction
DIRECTIONS = [(-1, -1), (-1, +0), (-1, +1),
              (+0, -1),           (+0, +1),
              (+1, -1), (+1, +0), (+1, +1)]


class Cell(object):
    """Manage the Othelo board cells."""

    def __init__(self, x, y, value="."):
        """Initiate the cell."""
        # Cell coordinates on the board
        self.x = x
        self.y = y
        # Cell value on the board among ".", "0", "B" and "W"
        self.value = value
        # Keep direction from DIRECTIONS only if next cell from current cell on this direction is inside the board
        self.directions = [direction for direction in DIRECTIONS
                           if 0 <= x + direction[0] < 8 and 0 <= y + direction[1] < 8]
