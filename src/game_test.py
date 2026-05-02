

class Board:

    def __init__(self):
        self.board = [" " for _ in range(42)]
        self.human_player = "O"
        self.ai_player = "X"

    def print_board(self):
        for i in range(0, 42, 7):
            print(f"  {self.board[i]}  |  {self.board[i+1]}  |  {self.board[i+2]}  |  {self.board[i+3]}  |  {self.board[i+4]}  |  {self.board[i+5]}  |  {self.board[i+6]} ")
            if i < 35:
                print("-" * 41)

    def available_grid_positions(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
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
                    print(f"{self.board[i]}, You've won!")
            
            #check column
            if i + 27 < 42:
                if self.board[i] == self.board[i + 7] == self.board[i + 14] == self.board[i + 21] != " ":
                    print(f"{self.board[i]}, You've won!")
                
            #check diagonals
            if i % 7 <= 3 and i + 24 < 42:
                if self.board[i] == self.board[i + 8] == self.board[i + 16] == self.board[i + 24] != " ":
                    print(f"{self.board[i]}, You've won!")
            if i % 7 >= 3 and i + 18 < 42:
                if self.board[i] == self.board[i + 6] == self.board[i + 12] == self.board[i + 18] != " ":
                    print(f"{self.board[i]}, You've won!")
        
        return None
    

    def game_over(self):
        return self.check_winner() is not None or self.is_board_full()
    
    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        if winner == self.ai_player:
            return 1
        if winner == self.human_player:
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for move in self.available_grid_positions():
                self.board[move] = self.ai_player
                score = self.minimax(depth + 1, False)
                self.board[move] = " "


board = Board()

board.drop_piece(0, "X")
board.drop_piece(0, "X")
board.drop_piece(0, "X")
board.drop_piece(0, "X")
board.drop_piece(1, "O")


board.print_board()


check = board.available_grid_positions()
board.check_winner()
     
print(check)