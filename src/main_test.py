from game_test import Board

board = Board()

class Game:

    def play_game(self):
        import random
        ai_turn = random.choice([True, False])

        while not self.game_over():
            board.print_board()

            if ai_turn:
                print("\n AI's turn...")
                col = board.get_best_move()
                board.drop_piece(col, board.ai_player)
            
            else:
                while True:
                    try:
                        col = int(input("Choose column (0-6): "))
                        if 0 <= col <= 8 and board.drop_piece(col, board.human_player):
                            break
                        else:
                            print("Invalid move! Try again.")

                    except ValueError:
                        print("Please enter a number between 0 and 8")

            ai_turn = not ai_turn

        board.print_board()
        winner = board.check_winner()
        if winner == board.ai_player:
            print("\nAI wins!")
        elif winner == board.human_player:
            print("\nCongratulations! You win!")
        else:
            print("\nIt's a tie!")
