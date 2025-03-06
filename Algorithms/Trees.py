import collections

def bfs_print(graph, current):
    print("BFS")
    visited, queue = set(), collections.deque([current])
    visited.add(current)

    while queue:
        d = queue.popleft()
        print(d, end=" ")
        if d in graph:
            for child in graph[d]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
    print()

def dfs_print(graph, current):
    print("DFS")
    visited, stack = set(), [current]

    while stack:
        d = stack.pop()
        if d not in visited:
            visited.add(d)
            print(d, end=" ")
            if d in graph:
                stack.extend(reversed(graph[d]))
    print()

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 2), ('G', 5)],
    'D': [('H', 10), ('I', 3), ('K', 8)]
}

gr2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

gr3 = {0: [1, 2],
       1: [3, 4],
       2: [5, 6],
       3: [7, 8]}

dfs_print(gr3, 0)
bfs_print(gr3, 0)

