import numpy as np

class SudokuSolver:
    solutions = []
    board = []

    # takes the sudoku board numbers as input from the user and assigns them to instance variable board
    def __init__(self):
        for i in range(0, 9):
            row = input('enter the numbers on row '+ str(i+1)+ ' of your sudoku board, enter 0 for empty squares and comma between every two squares and after every row hit enter\n')
            row = row.split(',')
            row = list(map(int, row))
            self.board.append(row)

    # checks if the number is allowed in the row point
    def allowed_row(self, x, y, n):
        if n in self.board[y]:
            return False
        else:
            return True

    # checks if the number is allowed in the column of the poing
    def allowed_column(self, x, y, n):
        for row in self.board:
            if n == row[x]:
                return False
        return True

    # checks if the number is allowed in the sqaure of the point
    def allowed_square(self, x, y, n):
        temp_board = self.board[(y//3)*3:(y//3)*3+3]

        temp_board = [row[(x//3)*3:(x//3)*3+3] for row in temp_board]

        for row in temp_board:
            if n in row:
                return False
        return True

    def allowed(self, x, y, n, board):
        if self.allowed_row(x, y, n) and self.allowed_column(x, y, n) and self.allowed_square(x, y, n):
            return True

        return False


    def solve(self):
        for y in range(9):
            for x in range(9):
    
                if self.board[y][x]==0:

                    for n in range(1, 10):
                        if self.allowed(x, y, n, self.board):
                            self.board[y][x] = n
                            
                            self.solve()
                            
                            self.board[y][x] = 0
                    return

        # took only the values of the lists to avoid the solutions variable changing with the change of the board
        self.solutions.append([list(row) for row in self.board])


# test
sudokuSolver = SudokuSolver()
sudokuSolver.solve()

print(np.matrix(sudokuSolver.solutions[0]))
