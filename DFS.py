class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited):
    if start not in visited:
        print("Visiting:", start)
        visited.add(start)

        for neighbor in graph.graph[start]:
            dfs(graph, neighbor, visited)

g = Graph()
g.add_edge('A', ['B', 'C'])
g.add_edge('B', ['A', 'D'])
g.add_edge('C', ['A', 'D'])
g.add_edge('D', ['B', 'C'])


start_node = 'A'
visited_nodes = set()
dfs(g, start_node, visited_nodes)
