from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        current_cost, current_node = priority_queue.get()

        if current_node in visited:
            continue

        print("Visiting:", current_node)
        visited.add(current_node)

        if current_node == goal:
            print("Goal reached!")
            break

        for neighbor, cost in graph.graph[current_node].items():
            if neighbor not in visited:
                priority_queue.put((cost, neighbor))

g = Graph()
g.add_edge('A', {'B': 4, 'C': 2})
g.add_edge('B', {'A': 4, 'D': 5})
g.add_edge('C', {'A': 2, 'D': 1})
g.add_edge('D', {'B': 5, 'C': 1})

start_node = 'A'
goal_node = 'D'
best_first_search(g, start_node, goal_node)
