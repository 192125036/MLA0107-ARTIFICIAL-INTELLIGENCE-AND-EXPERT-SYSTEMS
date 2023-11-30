class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.current_position = (0, 0)

    def move_up(self):
        if self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])

    def move_down(self):
        if self.current_position[0] < self.rows - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])

    def move_left(self):
        if self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)

    def move_right(self):
        if self.current_position[1] < self.cols - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)

    def clean_current_cell(self):
        if self.grid[self.current_position[0]][self.current_position[1]] == 'D':
            print(f"Cleaning cell at position {self.current_position}")
            self.grid[self.current_position[0]][self.current_position[1]] = 'C' 

    def is_dirty(self):
        return self.grid[self.current_position[0]][self.current_position[1]] == 'D'

    def clean_grid(self):
        while any('D' in row for row in self.grid):
            self.clean_current_cell()

            if self.is_dirty():
                print(f"Moving to the next dirty cell.")
            else:
                print("No more dirty cells in the current row. Moving to the next row.")
            
            if self.current_position[1] < self.cols - 1:
                self.move_right()
            else:
                self.move_down()
                self.current_position = (self.current_position[0], 0) 

grid = [
    ['D', 'C', 'D', 'C'],
    ['C', 'C', 'D', 'C'],
    ['D', 'C', 'C', 'D'],
    ['C', 'D', 'C', 'C']
]

vacuum = VacuumCleaner(grid)
vacuum.clean_grid()
