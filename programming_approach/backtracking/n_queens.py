from algo_fermat_utils.helpers import measure_performance


def n_queens(board, queens, target):
    # base case: if all queens have been placed, return True
    if queens == target:
        return True
    # try placing the next queen in each row of the board
    for row in range(target):
        # check if it is safe to place the queen in this position
        if is_valid(board, row, queens):
            # place the queen
            board[row][queens] = 1
            # recursively check if the remaining queens can be placed
            if n_queens(board, queens + 1, target):
                return True
            # backtrack: remove the queen and try a different placement
            board[row][queens] = 0
    # if no placement is possible, return False
    return False


def is_valid(board, row, queens):
    # check if any queen in the same column attacks the current position
    for i in range(queens):
        if board[row][i] == 1:
            return False
    # check if any queen in a diagonal attacks the current position
    for i in range(queens):
        if row - i >= 0 and board[row - i][queens - i] == 1:
            return False
        if row + i < len(board) and board[row + i][queens - i] == 1:
            return False
    return True


if __name__ == '__main__':
    # create a 2D array of size 8 x 8
    board = [[0 for i in range(8)] for j in range(8)]
    board[0][0] = 1  # place the first queen in the first row

    print("Result: ", n_queens(board, 3, 7))
