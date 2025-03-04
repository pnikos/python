# Depth First Search O(V+E) V=vertices/nodes, E=edges/branches
# Used in maze solving algorithms
def dfs_recursive(tree, node, visited=None):
    if visited == None:
        visited = set()
    visited.add(node)
    print(node)
    for child in tree[node]:
        if child not in visited:
            dfs_recursive(tree, child, visited)

def dfs_iterative(tree, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(tree[node]))


# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

dfs_recursive(tree, 'A')

dfs_iterative(tree, 'A')