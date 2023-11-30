from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def astar(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start, []))

    while not priority_queue.empty():
        current_cost, current_node, path = priority_queue.get()

        if current_node in visited:
            continue

        visited.add(current_node)

        path = path + [current_node]

        if current_node == goal:
            return path

        for neighbor, cost in graph.graph[current_node].items():
            if neighbor not in visited:
                priority_queue.put((current_cost + cost + heuristic(neighbor, goal), neighbor, path))

    return None

def heuristic(node, goal):

    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


g = Graph()
g.add_edge((0, 0), {(0, 1): 1, (1, 0): 1})
g.add_edge((0, 1), {(0, 0): 1, (1, 1): 1})
g.add_edge((1, 0), {(0, 0): 1, (1, 1): 1})
g.add_edge((1, 1), {(0, 1): 1, (1, 0): 1})


start_node = (0, 0)
goal_node = (1, 1)
path = astar(g, start_node, goal_node)

if path:
    print("Shortest Path:", path)
else:
    print("No path found.")
