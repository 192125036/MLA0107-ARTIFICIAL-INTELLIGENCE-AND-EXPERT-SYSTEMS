import random

def hill_climbing(problem, max_iterations=1000):
    current_solution = problem.initial_solution()
    current_value = problem.evaluate(current_solution)

    for _ in range(max_iterations):
        neighbors = problem.get_neighbors(current_solution)
        if not neighbors:
            break  
        next_solution = max(neighbors, key=problem.evaluate)
        next_value = problem.evaluate(next_solution)

        if next_value <= current_value:
            break  
        current_solution, current_value = next_solution, next_value

    return current_solution

class HillClimbingProblem:
    def __init__(self):
    
        pass

    def initial_solution(self):
        
        pass

    def evaluate(self, solution):
        
        pass

    def get_neighbors(self, solution):
        
        pass

class ExampleProblem(HillClimbingProblem):
    def initial_solution(self):
        return random.randint(0, 100)

    def evaluate(self, solution):
        return -abs(solution - 50)

    def get_neighbors(self, solution):
        return [solution + 1, solution - 1]

if __name__ == "__main__":
    problem = ExampleProblem()
    final_solution = hill_climbing(problem)

    print("Final Solution:", final_solution)
    print("Final Value:", problem.evaluate(final_solution))
