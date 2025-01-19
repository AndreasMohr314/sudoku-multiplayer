# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# This module generates Sudoku boards and their solutions based on a given difficulty level. 
# The `generate_sudoku` function creates an incomplete Sudoku board and its solution.

from sudoku import Sudoku

def generate_sudoku(difficulty_level):

    # Create a Sudoku puzzle (3x3 subgrids)
    sudoku = Sudoku(3).difficulty(difficulty_level)  # Difficulty level between 0.0 and 1.0
    board = sudoku.board  # The incomplete Sudoku board
    solution = sudoku.solve().board  # The complete solution
    return board, solution

