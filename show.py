def display(board):
    print()                              # blank line for spacing
    for i in range(3):                   # three rows
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("---+---+---")         # row separator
    print()
