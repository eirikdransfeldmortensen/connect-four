

class Board:

    def __init__(self):
        self.board = [" " for _ in range(42)]
        self.human_player = "O"
        self.ai_player = "X"

    def print_board(self):
        for i in range(0, 42, 7):
            print(f"\n  {self.board[i]}  |  {self.board[i+1]}  |  {self.board[i+2]}  |  {self.board[i+3]}  |  {self.board[i+4]}  |  {self.board[i+5]}  |  {self.board[i+6]} ")
            if i < 35:
                print("-" * 41)

    def available_columns(self):
        return [col for col in range(7) if self.board[col] == " "]
    
    def drop_piece(self, column, player):
        for row in range(5, -1, -1):
            index = row * 7 + column
            if self.board[index] == " ":
                self.board[index] = player
                return True
        return False
    
    def is_board_full(self):
        return " " not in self.board
    
    def check_winner(self):
        for i in range(42):
            if self.board[i] == " ":
                continue

            #check rows
            if i % 7 <= 3:
                if self.board[i] == self.board[i + 1] == self.board[i + 2] == self.board[i + 3] != " ":
                    return self.board[i]
            
            #check column
            if i + 21 < 42:
                if self.board[i] == self.board[i + 7] == self.board[i + 14] == self.board[i + 21] != " ":
                    return self.board[i]
                
            #check diagonals
            if i % 7 <= 3 and i + 24 < 42:
                if self.board[i] == self.board[i + 8] == self.board[i + 16] == self.board[i + 24] != " ":
                    return self.board[i]
            if i % 7 >= 3 and i + 18 < 42:
                if self.board[i] == self.board[i + 6] == self.board[i + 12] == self.board[i + 18] != " ":
                    return self.board[i]
        
        return None
    

    def game_over(self):
        return self.check_winner() is not None or self.is_board_full()
    
    def minimax(self, depth, is_maximizing, max_depth = 9, alpha=float("-inf"), beta=float("inf")):
        winner = self.check_winner()
        if winner == self.ai_player:
            return 10 - depth
        if winner == self.human_player:
            return depth - 10
        if self.is_board_full():
            return 0
        if depth >= max_depth:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for col in self.available_columns():
                self.drop_piece(col, self.ai_player) 
                score = self.minimax(depth + 1, False, max_depth, alpha, beta)
                self.undo_drop(col)
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        
        else:
            #if next turn is human, we want to minimize their score
            best_score = float("inf")
            for col in self.available_columns():
                self.drop_piece(col, self.human_player)
                score = self.minimax(depth + 1, True, max_depth, alpha, beta)
                self.undo_drop(col)
                best_score  = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
    
    def undo_drop(self, column):
        for row in range(6):
            index = row * 7 + column
            if self.board[index] != " ":
                self.board[index] = " "
                return
        
    
    def get_best_col(self):
        import random
        best_score = float("-inf")
        best_cols = []

        for col in self.available_columns():
            print(f"\nEvaluating column {col}...")
            self.drop_piece(col, self.ai_player)
            score = self.minimax(0, False)
            self.undo_drop(col)
            print(f"column {col} scored: {score}")
            if score > best_score:
                best_score = score
                best_cols = [col]
            elif score == best_score:
                best_cols.append(col)
                print(f"AI chose {col}")

        return random.choice(best_cols)
    
    def play_game(self):
        import random
        ai_turn = random.choice([True, False])
        print("\nSetting up board...")
        while not self.game_over():
            self.print_board()

            if ai_turn:
                print("\n AI's turn...")
                col = self.get_best_col()
                self.drop_piece(col, self.ai_player)
            
            else:
                while True:
                    try:
                        col = int(input("\nChoose column (0-6): "))
                        if 0 <= col <= 8 and self.drop_piece(col, self.human_player):
                            break
                        else:
                            print("Invalid move! Try again.")

                    except ValueError:
                        print("Please enter a number between 0 and 8")

            ai_turn = not ai_turn

        self.print_board()
        winner = self.check_winner()
        if winner == self.ai_player:
            print("\nAI wins!")
        elif winner == self.human_player:
            print("\nCongratulations! You win!")
        else:
            print("\nIt's a tie!")

if __name__ == "__main__":
    game = Board()
    game.play_game()
