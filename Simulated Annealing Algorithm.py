import math
import random

def initial_solution():
  
    return random.uniform(-10, 10)

def objective_function(x):

    return x**2  

def acceptance_probability(old_cost, new_cost, temperature):
  
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing(iterations, initial_temperature, cooling_rate):
    current_solution = initial_solution()
    current_cost = objective_function(current_solution)

    best_solution = current_solution
    best_cost = current_cost

    temperature = initial_temperature

    for _ in range(iterations):
        new_solution = current_solution + random.uniform(-0.5, 0.5)  # Example: small perturbation
        new_cost = objective_function(new_solution)

        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_solution = new_solution
            current_cost = new_cost

        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost

        temperature *= 1 - cooling_rate

    return best_solution, best_cost

iterations = 1000
initial_temperature = 1000.0
cooling_rate = 0.03

best_solution, best_cost = simulated_annealing(iterations, initial_temperature, cooling_rate)

print("Best Solution:", best_solution)
print("Best Cost:", best_cost)
