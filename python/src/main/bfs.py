from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes.
    queue = deque([start])  # Queue for BFS, initialized with the start node

    while queue:
        vertex = queue.popleft()  # Remove the leftmost (earliest added) element
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")  # Process the current node

            # Add unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A')  # Starting BFS from node 'A'
