import heapq
from collections import defaultdict

def min_cost_max_flow(graph, source, sink):
    """
    Implementation of the minimum cost maximum flow algorithm with capacity constraints.
    
    :param graph: Dictionary containing the graph with capacity and cost constraints.
    :param source: Source node.
    :param sink: Sink node.
    :return: A tuple containing the maximum flow and the minimum cost.
    """
    
    # Residual graph with all capacities initially set to 0 and costs to infinity
    residual_graph = defaultdict(lambda: defaultdict(int))
    for node in graph:
        for neighbor in graph[node]:
            residual_graph[node][neighbor] = graph[node][neighbor][0]
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
    
    # Find minimum cost using Dijkstra's algorithm
    def dijkstra(graph, start, end):
        distances = {node: float("inf") for node in graph}
        distances[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor in graph[current_node]:
                cost = graph[current_node][neighbor][1]
                if residual_graph[current_node][neighbor] > 0 and distances[neighbor] > distances[current_node] + cost:
                    distances[neighbor] = distances[current_node] + cost
                    parent[neighbor] = current_node
                    heapq.heappush(queue, (distances[neighbor], neighbor))
        return distances[end]
    
    # Find maximum flow and minimum cost using Bellman-Ford algorithm
    max_flow = 0
    min_cost = 0
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
            min_cost += path_flow * graph[parent[current_node]][current_node][1]
            current_node = parent[current_node]
    
    return (max_flow, min_cost)

graph = {
    's': {'a': (3, 1), 'b': (2, 5)},
    'a': {'b': (1, 2), 'c': (5, 1), 'd': (4, 2)},
    'b': {'d': (2, 2)},
    'c': {'t': (2, 5)},
    'd': {'c': (1, 1), 't': (3, 3)},
    't': {}
}

max_flow, min_cost = min_cost_max_flow(graph, 's', 't')
print("Maximum flow:", max_flow)
print("Minimum cost:", min_cost)