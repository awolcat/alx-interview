#!/usr/bin/python3
"""nqueens
    for a board size n*n, how many ways
    can you fit n queens so that no queen is
    attacking another..
"""
import sys


def validate_args():
    """Validate command line args for nqueens
    """
    if len(sys.argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    finally:
        if N < 4:
            print('N must be at least 4')
            exit(1)
        return N


def nqueens(n):
    """N Queens Problem Solution
    """
    col = set()  # holds occupied columns
    posDiag = set()  # occupied positive diagonals /
    negDiag = set()  # occupied negative diagonals \

    sol = []
    board = []

    def backtrack(r):
        """Abracadabra
        """
        if r == n:
            copy = board.copy()
            sol.append(copy)
            print(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board.append([r, c])

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board.remove([r, c])
    backtrack(0)
    return sol


if __name__ == '__main__':
    """Module runner
    """
    rows = validate_args()
    nqueens(rows)
    # solution = nqueens(rows)
    # print(solution)
