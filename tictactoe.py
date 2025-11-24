import numpy as np


def tictactoe():
    """This functions takes no arguements and when called it will prompt the interface to play
    with AI. ONLY USING NUMPY."""
    print("Who will play first?\nAI - 'X' - press X\nor\nI  - 'O' - press O")
    choice = str(input("X or O : "))

    # Making the board
    board = np.zeros((3, 3), dtype=int)  # 0 - empty, 1 - AI, -1 - I

    if choice not in ["X", "O"]:
        print("Invalid choice. Try again.")
        tictactoe()
        return

    board = compete(choice, board)
    cw = checkwinner(board)
    if cw == 3:
        print("AI won.")
        return
    elif cw == -3:
        print("I won.")
        return


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


def compete(choice, board):
    if choice == "O":
        ipos = int(input("Which position for your move 1 - 9 : "))
        if ipos not in range(1, 10):
            compete(choice=choice, board=board)
            return
        ipos_index = indexized(ipos)
        board[ipos_index] = -1
        print("I choose this one : \n")
        print(board)
        return board
    if choice == "X":
        apos = predict(board)
        return board


def empty_positions(board):
    """Return a list of (row, col) tuples where board is empty (0)"""
    return [(r, c) for r in range(3) for c in range(3) if board[r, c] == 0]


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
        # print(vboard)
        result = checkwinner(vboard)
        spacetree[1][i][0] = result  # store result at this node

        # Recursively build children (next moves)
        spacetree[1][i][1] = spacetreefarm(vboard, -player)[1]  # children of this node

    return spacetree

    # count = 0
    # for branches in emptypos:
    #     r, c = branches
    #     vboard = board.copy()

    #     vboard[r, c] = 1
    #     check = checkwinner(vboard)
    #     spacetreestructure[9 - width][count] = check
    #     count += 1


def indexized(pos):
    """Convert 1-9 position to (row, col) index"""
    pos -= 1  # 1-9 → 0-8
    return (pos // 3, pos % 3)


def predict(board):
    # spacetreestructure = [np.zeros(n, dtype=int) for n in range(9, 0, -1)]
    # spacetree = spacetreefarm(board, spacetreestructure)

    spacetree = spacetreefarm(board)
    emptypos = empty_positions(board)
    width = len(emptypos)
    # print(len(spacetree))

    

    for node.n in spacetree[1]:
        if node.n == 3:
            


if __name__ == "__main__":
    tictactoe()
