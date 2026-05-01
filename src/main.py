from game import Board

board = Board()
current_player = 1

while True: 
    board.print_board()
    column_placement = int(input(f"\nPlayer {current_player}, choose a colum (0-6) "))

    if column_placement < 0 or column_placement > 6:
        print("\nInvalid column, choose between 0 and 6.")
        continue

    if board.drop_piece(column_placement, current_player):
        if board.check_win(current_player):
            board.print_board()
            print(f"Player {current_player} wins!")
            break
        current_player = 2 if current_player == 1 else 1
    else:
        print("Column is full, try again.")

    
    
    
    
