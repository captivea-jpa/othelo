import unittest

from models import Board, Cell


class TestBoardAndCell(unittest.TestCase):
    """Test Board and Cell classes."""

    def setUp(self) -> None:
        """Run this before every tests."""
        self.board = Board()
        self.directions = [(-1, -1), (-1, +0), (-1, +1),
                           (+0, -1),           (+0, +1),
                           (+1, -1), (+1, +0), (+1, +1)]

    def test_board_has_8_rows(self):
        """Board must have 8 rows."""
        self.assertEqual(8, len(self.board.rows), f"{self.board} has not 8 rows.")

    def test_board_row_has_8_elements(self):
        """Board row must have 8 elements."""
        for row in self.board.rows:
            self.assertEqual(8, len(row), f"{row} has not 8 elements.")

    def test_board_element_is_an_instance_of_cell_class(self):
        """Board element must be an instance of Cell class."""
        for row in self.board.rows:
            for element in row:
                self.assertIsInstance(element, Cell)

    def test_cell_coordinates_correspond_to_cell_position_in_board(self):
        """Cell coordinates must correspond to cell position in board."""
        for (i, row) in enumerate(self.board.rows):
            for (j, cell) in enumerate(row):
                self.assertEqual(i, cell.x, f"X coordinate of {cell} is not {i}.")
                self.assertEqual(j, cell.y, f"Y coordinate of {cell} is not {j}.")

    def test_cell_directions_are_directions_where_cell_has_neighbors(self):
        """Cell directions must be directions where cell has neighbors."""
        for (i, row) in enumerate(self.board.rows):
            for (j, cell) in enumerate(row):
                for direction in self.directions:
                    if 0 <= i + direction[0] < 8 and 0 <= j + direction[1] < 8:
                        message = f"{cell} has not {direction} in its directions."
                        self.assertIn(direction, cell.directions, message)
                    else:
                        message = f"{cell} has {direction} in its directions."
                        self.assertNotIn(direction, cell.directions, message)

    def test_next_cell_returns_coherent_value_in_all_directions(self):
        """Next cell must return coherent value in all directions."""
        for (i, row) in enumerate(self.board.rows):
            for (j, cell) in enumerate(row):
                for direction in self.directions:
                    if 0 <= i + direction[0] < 8 and 0 <= j + direction[1] < 8:
                        next_cell = self.board.rows[i + direction[0]][j + direction[1]]
                        message = f"Next cell from {cell} in {direction} does not return {next_cell}."
                        self.assertEqual(next_cell, self.board.next_cell(cell, direction), message)
                    else:
                        message = f"Next cell from {cell} in {direction} does not return None."
                        self.assertIsNone(self.board.next_cell(cell, direction), message)

    def test_board_has_4_playable_cells_initially(self):
        """Board must have 4 playable cells initially."""
        message = f"{self.board.rows[2][4]} is not playable initially"
        self.assertTrue(self.board.has_playable_cell(self.board.rows[2][4]), message)
        message = f"{self.board.rows[3][5]} is not playable initially"
        self.assertTrue(self.board.has_playable_cell(self.board.rows[3][5]), message)
        message = f"{self.board.rows[4][2]} is not playable initially"
        self.assertTrue(self.board.has_playable_cell(self.board.rows[4][2]), message)
        message = f"{self.board.rows[5][3]} is not playable initially"
        self.assertTrue(self.board.has_playable_cell(self.board.rows[5][3]), message)

    def test_playable_cells_returns_playable_cells_only(self):
        """Playable cells must return playable cells only."""
        for cell in self.board.playable_cells():
            message = f"{cell} is not playable but has been returned as if."
            self.assertTrue(self.board.has_playable_cell(cell), message)
