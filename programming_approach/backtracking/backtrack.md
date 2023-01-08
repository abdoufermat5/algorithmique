# Use cases

## 1. N-Queens Problem

Another example of a real-life problem that can be solved using backtracking is the "n-queens problem." Given an n-by-n
chessboard, the goal is to place n queens on the board such that no queen can attack any other queen. One way to solve
this problem is to use backtracking to explore all possible placements of the queens on the board and backtrack when a
placement leads to a dead end (i.e., a queen is placed in a position where it can attack another queen).

## 2. Sudoku Solver

Another example of a real-life problem that can be solved using backtracking is the "sudoku solver." Given a partially
filled-in sudoku board, the goal is to fill in the remaining empty cells such that each row, column, and 3-by-3 subgrid
contains all of the digits from 1 to 9. One way to solve this problem is to use backtracking to explore all possible
combinations of digits for the empty cells and backtrack when a combination leads to a dead end (i.e., a cell is filled in
with a digit that is already present in the same row, column, or 3-by-3 subgrid).

## 3. Word Search

Another example of a real-life problem that can be solved using backtracking is the "word search." Given a 2D grid of
characters and a word, the goal is to find all occurrences of the word in the grid. The word can be constructed from
characters of sequentially adjacent cells, where "adjacent" cells are those horizontally or vertically neighboring. The
same cell may not be used more than once. One way to solve this problem is to use backtracking to explore all possible
combinations of adjacent cells that form the word and backtrack when a combination leads to a dead end (i.e., a cell is
used more than once or the word constructed so far does not match the prefix of the target word).
