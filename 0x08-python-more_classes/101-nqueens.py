#!/usr/bin/python3
"""Solution for the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Examples:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    card (list): List of lists representing the chessboard.
    solutions (list): List of lists containing solutions.
Solutions are represented in the format [[r, d], [r, d], [r, d], [r, d]]
where `r` and `d` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Starting an `n`x`n` sized chessboard with 0's."""
    card = []
    [card.append([]) for t in range(n)]
    [row.append(' ') for t in range(n) for row in card]
    return (card)


def board_deepcopy(card):
    """Bring a deepcopy of a chessboard."""
    if isinstance(card, list):
        return list(map(board_deepcopy, card))
    return (card)


def get_solution(card):
    """Bring the list of lists representation of a solved chessboard."""
    solves = []
    for r in range(len(card)):
        for d in range(len(card)):
            if card[r][d] == "Q":
                solves.append([r, d])
                break
    return (solves)


def xout(card, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        card (list): Current working chessboard.
        row (int): Row where a queen was last played.
        col (int): Column where a queen was last played.
    """
    # X out all forward spots
    for d in range(col + 1, len(card)):
        card[row][d] = "x"
    # X out all backwards spots
    for d in range(col - 1, -1, -1):
        card[row][d] = "x"
    # X out all spots below
    for r in range(row + 1, len(card)):
        card[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        card[r][col] = "x"
    # X out all spots diagonally down to the right
    d = col + 1
    for r in range(row + 1, len(card)):
        if d >= len(card):
            break
        card[r][d] = "x"
        d += 1
    # X out all spots diagonally up to the left
    d = col - 1
    for r in range(row - 1, -1, -1):
        if d < 0:
            break
        card[r][d]
        d -= 1
    # X out all spots diagonally up to the right
    d = col + 1
    for r in range(row - 1, -1, -1):
        if d >= len(card):
            break
        card[r][d] = "x"
        d += 1
    # X out all spots diagonally down to the left
    d = col - 1
    for r in range(row + 1, len(card)):
        if d < 0:
            break
        card[r][d] = "x"
        d -= 1


def recursive_solve(card, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        card (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(card):
        solutions.append(get_solution(card))
        return (solutions)

    for d in range(len(card)):
        if card[row][d] == " ":
            tmp_board = board_deepcopy(card)
            tmp_board[row][d] = "Q"
            xout(tmp_board, row, d)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    card = init_board(int(sys.argv[1]))
    solutions = recursive_solve(card, 0, 0, [])
    for sol in solutions:
        print(sol)
