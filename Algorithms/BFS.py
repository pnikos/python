from collections import deque

# 1. Start with Node 1 in the queue
# 2. Visit Node 1, Add its neighbours
# 3. Remove Node 1 from front the queue
# 4. Node 2 is now at the front
# 5. Visit Node 2, enqueue its children
# 6. Remove Node 2 from front of the queue
# 7. Node 3 is now at the front
# ...
# The queue is empty, BFS is completed

# Better at finding nodes close to the root

# Breadth First Search O(V+E) V=vertices/nodes, E=edges/branches
# Used in chess algorithms
def bfs(tree, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],  # Node A connects to B and C
    'B': ['D', 'E'],  # Node B connects to D and E
    'C': ['F', 'G'],  # Node C connects to F and G
    'D': ['H', 'I'],  # Node D connects to H and I
    'E': ['J', 'K'],  # Node E connects to J and K
    'F': ['L', 'M'],  # Node F connects to L and M
    'G': ['N', 'O'],  # Node G connects to N and O
    'H': [], 'I': [], 'J': [], 'K': [],  # Leaf nodes have no children
    'L': [], 'M': [], 'N': [], 'O': []   # Leaf nodes have no children
}

bfs(tree, 'A')





