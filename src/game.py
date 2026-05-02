#import pygame


class Board:
    
    def __init__(self):
        self.num_rows = 6
        self.num_cols = 7
        self.grid = [[0 for _ in range(self.num_cols,)] for _ in range(self.num_rows)]

    def print_board(self):
        for row in self.grid:
          print(row)
    
    def drop_piece(self, column, current_player):
        for row in range(self.num_rows - 1, -1, -1,):
            if self.grid[row][column] == 0:
                self.grid[row][column] = current_player
                return True
        return False
    
    def check_win(self, current_player):
        for row in range(self.num_rows):
            for col in range(self.num_cols -3):
               if (self.grid[row][col] == current_player and
                self.grid[row][col+1] == current_player and
                self.grid[row][col+2] == current_player and
                self.grid[row][col+3] == current_player):
                return True

        for row in range(self.num_rows - 3):
            for col in range(self.num_cols):
                if (self.grid[row][col] == current_player and
                    self.grid[row+1][col] == current_player and
                    self.grid[row+2][col] == current_player and
                    self.grid[row+3][col] == current_player):
                    return True
        for row in range(self.num_rows - 3):
            for col in range(self.num_cols - 3):
                if (self.grid[row][col] == current_player and
                    self.grid[row+1][col+1] == current_player and
                    self.grid[row+2][col+2] == current_player and
                    self.grid[row+3][col+3] == current_player):
                    return True

        for row in range(3, self.num_rows):
            for col in range(self.num_cols - 3):
                if (self.grid[row][col] == current_player and
                    self.grid[row-1][col+1] == current_player and
                    self.grid[row-2][col+2] == current_player and
                    self.grid[row-3][col+3] == current_player):
                    return True
        return False
    
    def available_positions(self):
        return [(row, col) for row in range(self.num_rows)
                for col in range(self.num_cols)
                if self.grid[row][col] == 0]
    
board = Board()
board.print_board()
moves = board.available_positions()
print(moves)