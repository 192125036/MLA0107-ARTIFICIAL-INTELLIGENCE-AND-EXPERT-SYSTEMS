import sys
def nearest_neighbor(graph):
    num_cities = len(graph)
    visited = [False] * num_cities
    path = [0]  
    total_distance = 0
    for _ in range(num_cities - 1):
        current_city = path[-1]
        min_distance = sys.maxsize
        next_city = None
        for neighbor in range(num_cities):
            if not visited[neighbor] and graph[current_city][neighbor] < min_distance:
                min_distance = graph[current_city][neighbor]
                next_city = neighbor
        path.append(next_city)
        total_distance += min_distance
        visited[next_city] = True
    path.append(path[0])
    total_distance += graph[path[-2]][path[0]]
    return path, total_distance
cities = ["City A", "City B", "City C", "City D"]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, total_distance = nearest_neighbor(distances)

print("Shortest Path:", shortest_path)
print("Total Distance:", total_distance)
