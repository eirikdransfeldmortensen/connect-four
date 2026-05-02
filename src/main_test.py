from game_test import Board

board = Board()

while True:
    board.print_board()
    col_pla = int(input("Choose column (0-6): "))
    if not board.drop_piece(col_pla, board.human_player):
        print("Column is full, pick another!")

    if col_pla < 0 or col_pla > 6:
        print("\nInvalid column, choose between 0 and 6.")
        continue