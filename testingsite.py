import numpy as np


def make_zero_tree(dim):
    """
    Creates a decreasing-dimension recursive tree.
    Each node = [0, children]
    children = list of (dim-1) similar nodes.
    """
    if dim == 0:
        return [0, []]  # leaf node

    children = [make_zero_tree(dim - 1) for _ in range(dim)]
    return [0, children]


def empty_positions(board):
    """Return a list of (row, col) tuples where board is empty (0)"""
    return [(r, c) for r in range(3) for c in range(3) if board[r, c] == 0]


def checkwinner(b):
    winning_planks = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for plank in winning_planks:
        total = sum(b[r, c] for r, c in plank)
        if total == 3:
            return 3
        elif total == -3:
            return -3
    return 0


def spacetreefarm(board, player=1):
    """
    Recursively builds a spacetree for Tic-Tac-Toe:
    - Each node = [evaluation, children]
    - Children = all possible moves from current board
    """

    emptypos = empty_positions(board)
    width = len(emptypos)

    # If no empty positions, return leaf node
    if width == 0:
        result = checkwinner(board)
        return [result, []]

    # Create current level of the tree
    spacetree = make_zero_tree(width)

    for i, (r, c) in enumerate(emptypos):
        vboard = board.copy()
        vboard[r, c] = player  # simulate move

        # Evaluate the board
        result = checkwinner(vboard)
        spacetree[1][i][0] = result  # store result at this node

        # Recursively build children (next moves)
        spacetree[1][i][1] = spacetreefarm(vboard, -player)[1]  # children of this node

    return spacetree


board = [[-1, 1, 0], [0, 1, 0], [0, -1, -1]]
board = np.array(board, dtype=int)
spacetree = spacetreefarm(board)


def best_move_from_tree(tree, depth=0, maximizing=True):
    """
    Recursively find the best move from the tree.
    tree: [value, [children]]
    maximizing: True if AI's turn (1), False if Human (-1)
    Returns: (best_value, best_index)
    """
    value, children = tree

    # Leaf node: return its value
    if not children:
        return value, None

    best_index = None

    if maximizing:
        best_val = -float("inf")
        for i, child in enumerate(children):
            val, _ = best_move_from_tree(child, depth + 1, maximizing=False)
            if val > best_val:
                best_val = val
                best_index = i
        return best_val, best_index
    else:
        best_val = float("inf")
        for i, child in enumerate(children):
            val, _ = best_move_from_tree(child, depth + 1, maximizing=True)
            if val < best_val:
                best_val = val
                best_index = i
        return best_val, best_index


print(best_move_from_tree(spacetree))
