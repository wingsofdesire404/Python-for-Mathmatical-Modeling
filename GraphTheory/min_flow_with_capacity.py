from collections import defaultdict

def min_flow(graph, source, sink):
    """
    Implementation of the minimum flow algorithm with capacity constraints.
    
    :param graph: Dictionary containing the graph with capacity constraints.
    :param source: Source node.
    :param sink: Sink node.
    :return: The minimum flow from source to sink.
    """
    
    # Residual graph with all capacities initially set to 0
    residual_graph = defaultdict(lambda: defaultdict(int))
    for node in graph:
        for neighbor in graph[node]:
            residual_graph[node][neighbor] = graph[node][neighbor]
            residual_graph[neighbor][node] = 0
    
    # Parent dictionary for storing path from source to sink
    parent = {}
    
    # Breadth first search to find augmenting paths in residual graph
    def bfs(graph, start, end, parent):
        visited = defaultdict(bool)
        queue = [start]
        visited[start] = True
        
        while queue:
            current_node = queue.pop(0)
            for neighbor in graph[current_node]:
                if not visited[neighbor] and residual_graph[current_node][neighbor] > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current_node
                    if neighbor == end:
                        return True
        return False
    
    # Find maximum flow using Ford-Fulkerson algorithm
    max_flow = 0
    while bfs(residual_graph, source, sink, parent):
        path_flow = float("Inf")
        current_node = sink
        while current_node != source:
            path_flow = min(path_flow, residual_graph[parent[current_node]][current_node])
            current_node = parent[current_node]
        max_flow += path_flow
        current_node = sink
        while current_node != source:
            residual_graph[parent[current_node]][current_node] -= path_flow
            residual_graph[current_node][parent[current_node]] += path_flow
            current_node = parent[current_node]
    
    return max_flow

graph = {
    0: {1: 16, 2: 13}, # from 0 to 1 with capacity = 16 and from 0 to 2 with capacity = 13
    1: {2: 10, 3: 12},
    2: {1: 4, 4: 14},
    3: {2: 9, 5: 20},
    4: {3: 7, 5: 4},
    5: {}
}

source = 0
sink = 5

min_flow = min_flow(graph, source, sink)
print("The minimum flow from", source, "to", sink, "is", min_flow)

