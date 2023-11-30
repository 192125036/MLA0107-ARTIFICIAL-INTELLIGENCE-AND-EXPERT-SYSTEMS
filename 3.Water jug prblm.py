class WaterJugProblem:
    def __init__(self, jug_4_capacity, jug_3_capacity, target_amount):
        self.jug_4_capacity = jug_4_capacity
        self.jug_3_capacity = jug_3_capacity
        self.target_amount = target_amount
        self.jug_4 = 0
        self.jug_3 = 0
    def fill_jug_4(self):
        self.jug_4 = self.jug_4_capacity
    def fill_jug_3(self):
        self.jug_3 = self.jug_3_capacity
    def pour_jug_4_to_jug_3(self):
        transfer = min(self.jug_4, self.jug_3_capacity - self.jug_3)
        self.jug_4 -= transfer
        self.jug_3 += transfer
    def pour_jug_3_to_jug_4(self):
        transfer = min(self.jug_3, self.jug_4_capacity - self.jug_4)
        self.jug_3 -= transfer
        self.jug_4 += transfer
    def empty_jug_4(self):
        self.jug_4 = 0
    def empty_jug_3(self):
        self.jug_3 = 0
    def is_goal_reached(self):
        return self.jug_4 == self.target_amount
    def solve(self):
        while not self.is_goal_reached():
            print(f"Jug 4: {self.jug_4} gallons, Jug 3: {self.jug_3} gallons")
            if self.jug_4 == 0:
                self.fill_jug_4()
            elif self.jug_3 == self.jug_3_capacity:
                self.empty_jug_3()
            elif self.jug_4 > 0 and self.jug_3 < self.jug_3_capacity:
                self.pour_jug_4_to_jug_3()
        print(f"Jug 4: {self.jug_4} gallons, Jug 3: {self.jug_3} gallons")
        print("Goal reached! Exactly 2 gallons of water in the 4-gallon jug.")
water_problem = WaterJugProblem(jug_4_capacity=4, jug_3_capacity=3, target_amount=2)
water_problem.solve()
