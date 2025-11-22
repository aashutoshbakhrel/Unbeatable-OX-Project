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
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],

    # Columns
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],

    # Diagonals
    [(0,0),(1,1),(2,2)],
    [(0,2),(1,1),(2,0)]
    ]

    for plank in winning_planks:
        total = sum(b[r, c] for r, c in plank)
        if total == 3:
            return 3
        elif total == -3:
            return -3




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
        aipos = predict(board)


def predict(board):
    

def indexized(pos):
    """Convert 1-9 position to (row, col) index"""
    pos -= 1  # 1-9 → 0-8
    return (pos // 3, pos % 3)


if __name__ == "__main__":
    tictactoe()
