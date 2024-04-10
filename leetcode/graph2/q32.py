def dfs(graph, node, visited, connected_component):
    if node not in visited:
        visited.add(node)
        connected_component.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited, connected_component)

def find_connected_pairs(pairs):
    graph = {}
    # Create an adjacency list representation of the graph
    for pair in pairs:
        if pair[0] not in graph:
            graph[pair[0]] = []
        if pair[1] not in graph:
            graph[pair[1]] = []
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])

    connected_pairs = []
    visited = set()
    for node in graph:
        if node not in visited:
            connected_component = []
            dfs(graph, node, visited, connected_component)
            connected_pairs.append(sorted(connected_component))

    return connected_pairs

pairs = [[0,3],[1,2]]
connected_pairs = find_connected_pairs(pairs)
print("Connected pairs:")
for pair in connected_pairs:
    print(pair)
