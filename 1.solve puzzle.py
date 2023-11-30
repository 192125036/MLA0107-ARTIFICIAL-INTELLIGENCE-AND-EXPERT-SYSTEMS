class SlidingPuzzle:
    def __init__(self):
        self.board = [[8, 7, 6],
                      [5, 4, 3],
                      [2, 1, None]]
    def display(self):
        for row in self.board:
            print(row)
        print()
    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return i, j
    def move(self, direction):
        empty_row, empty_col = self.find_empty()
        if direction == "up" and empty_row > 0:
            self.board[empty_row][empty_col], self.board[empty_row - 1][empty_col] = (
                self.board[empty_row - 1][empty_col],
                self.board[empty_row][empty_col],
            )
        elif direction == "down" and empty_row < 2:
            self.board[empty_row][empty_col], self.board[empty_row + 1][empty_col] = (
                self.board[empty_row + 1][empty_col],
                self.board[empty_row][empty_col],
            )
        elif direction == "left" and empty_col > 0:
            self.board[empty_row][empty_col], self.board[empty_row][empty_col - 1] = (
                self.board[empty_row][empty_col - 1],
                self.board[empty_row][empty_col],
            )
        elif direction == "right" and empty_col < 2:
            self.board[empty_row][empty_col], self.board[empty_row][empty_col + 1] = (
                self.board[empty_row][empty_col + 1],
                self.board[empty_row][empty_col],
            )
        else:
            print("Invalid move")
    def is_solved(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, None]]
puzzle = SlidingPuzzle()
while not puzzle.is_solved():
    puzzle.display()
    move_direction = input("Enter move direction (up/down/left/right): ")
    puzzle.move(move_direction)
print("Puzzle solved!")
