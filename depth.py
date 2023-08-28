# Depth-First Search (DFS) on Graph
def dfs(graph, node, visited):
    if not visited[node]:
        visited[node] = True
        print("Visiting node:", node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited)

# Example usage
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}
start_node = 1
visited = [False] * (len(graph) + 1)
dfs(graph, start_node, visited)
