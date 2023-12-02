class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_location = (0, 0)  
        self.box_location = (1, 0)    
        self.banana_location = (2, 2) 
    def move_monkey(self, direction):
        x, y = self.monkey_location
        if direction == 'up' and x > 0:
            self.monkey_location = (x - 1, y)
        elif direction == 'down' and x < 2:
            self.monkey_location = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.monkey_location = (x, y - 1)
        elif direction == 'right' and y < 2:
            self.monkey_location = (x, y + 1)
    def move_box(self, direction):
        x, y = self.box_location
        if direction == 'up' and x > 0:
            self.box_location = (x - 1, y)
        elif direction == 'down' and x < 2:
            self.box_location = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.box_location = (x, y - 1)
        elif direction == 'right' and y < 2:
            self.box_location = (x, y + 1)
    def is_goal_state(self):
        return self.monkey_location == self.banana_location and self.box_location == self.banana_location
    def __str__(self):
        return f"Monkey: {self.monkey_location}, Box: {self.box_location}, Banana: {self.banana_location}"
def solve_monkey_banana_problem():
    problem = MonkeyBananaProblem()
    actions = ['right', 'up', 'up', 'left', 'left', 'down', 'down', 'right', 'right']
    for action in actions:
        problem.move_monkey(action)
        print(problem)
        if problem.is_goal_state():
            print("Monkey reached the bananas!")
            break
    if not problem.is_goal_state():
        print("Monkey couldn't reach the bananas.")

if __name__ == "__main__":
    solve_monkey_banana_problem()
