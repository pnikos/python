import heapq

def dijkstra(graph, start):
    """
    Finds the shortest path from the start node to all other nodes in the graph.

    :param graph: A dictionary where keys are nodes and values are lists of (neighbor, weight) tuples.
    :param start: The starting node.
    :return: A dictionary with the shortest distance to each node from the start node.
    """
    # Priority queue for min-heap (distance, node)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}  # Initialize distances as infinity
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If the current distance is greater than the recorded distance, skip processing
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If found a shorter path, update and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example Graph (Adjacency List Representation)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3), ('E', 8)],
    'E': [('D', 8)]
}

# Run Dijkstra's algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
