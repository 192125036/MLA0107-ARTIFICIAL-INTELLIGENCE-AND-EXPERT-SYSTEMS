class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def greedy_coloring(self):
        colors = {}
        color_count = 0

        for node in self.graph:
            neighbor_colors = set(colors.get(neighbor, None) for neighbor in self.graph[node])
            available_colors = set(range(color_count + 1)) - neighbor_colors

            if not available_colors:
                color_count += 1
                colors[node] = color_count
            else:
                colors[node] = min(available_colors)

        return colors

def print_colored_map(colors):
    color_map = {
        0: 'Red',
        1: 'Green',
        2: 'Blue',
        # Add more colors as needed
    }

    for node, color in colors.items():
        print(f"Region {node} is colored {color_map[color]}")

# Example usage:
if __name__ == "__main__":
    graph = Graph()

    # Add edges between adjacent regions
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    # Perform greedy coloring
    coloring_result = graph.greedy_coloring()

    # Print the colored map
    print_colored_map(coloring_result)
