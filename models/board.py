from .cell import Cell

# OPPONENTS is a dictionary returning the opponent player of a player, for each players
OPPONENTS = {"B": "W", "W": "B"}


def display(rows, player):
    """Display a bunch of rows full of 'Cell' instances, then a player."""
    for row in rows:
        print(" ".join([cell.value for cell in row]))
    print(player + "\n")


class Board(object):
    """Manage the Othelo board."""

    def __init__(self):
        """Initiate the board."""
        # Board cells by row
        self.rows = [[Cell(i, j) for j in range(8)] for i in range(8)]
        self.rows[3][3].value = self.rows[4][4].value = "B"
        self.rows[3][4].value = self.rows[4][3].value = "W"
        # Current player
        self.player = "B"

    def display(self):
        """Display the board."""
        display(self.rows, self.player)

    def next_cell(self, cell, direction):
        """Return the next cell of the board from the given cell in the given direction, None otherwise."""
        # Next cell coordinates
        x = cell.x + direction[0]
        y = cell.y + direction[1]
        # Next cell has to be inside the board
        if 0 <= x < 8 and 0 <= y < 8:
            return self.rows[x][y]
        return None

    def playable_cell(self, cell):
        """Return True if the given cell is playable for the current player, False otherwise."""
        # Return True if the cell is already marked as playable
        if cell.value == "0":
            return True
        # Otherwise, return False if the cell is not empty
        if cell.value != ".":
            return False
        # Now, we are looking around an empty cell for each of all possible directions
        for direction in cell.directions:
            # First next cell in that direction has to be taken by the opponent of current player
            next_cell = self.next_cell(cell, direction)
            if next_cell.value != OPPONENTS[self.player]:
                continue
            # Other cells in that direction must be composed of, in that precise order:
            # - a potential series of cells already taken by the opponent player of current player
            # - at least one cell already taken by the current player
            next_cell = self.next_cell(next_cell, direction)
            while next_cell:
                # Change direction if we find an empty cell in the process
                if next_cell.value in [".", "0"]:
                    break
                # If we find the cell already taken by current player, its winner winner chicken dinner!
                elif next_cell.value == self.player:
                    return True
                # Otherwise, continue to search among the next cells
                next_cell = self.next_cell(next_cell, direction)
        # In the end, if cell does not respect criteria, return False
        return False

    def playable_cells(self):
        """Yield a list of the playable cells for current player."""
        for row in self.rows:
            for cell in row:
                if self.playable_cell(cell):
                    yield cell

    def display_with_help(self):
        """Display the board whit indications where the current player can play."""
        for cell in self.playable_cells():
            cell.value = "0"
        display(self.rows, self.player)
        for cell in self.playable_cells():
            cell.value = "."
