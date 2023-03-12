import networkx as nx

# 创建有向无环图
G = nx.DiGraph()

# 添加节点
G.add_node('A', duration=3)
G.add_node('B', duration=2)
G.add_node('C', duration=4)
G.add_node('D', duration=5)
G.add_node('E', duration=2)
G.add_node('F', duration=3)
G.add_node('G', duration=2)

# 添加边
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('D', 'F')
G.add_edge('E', 'G')
G.add_edge('F', 'G')

# 计算最早开始时间
earliest_start_time = {}
for node in nx.topological_sort(G):
    earliest_start_time[node] = max([earliest_start_time.get(pred, 0) for pred in G.predecessors(node)], default=0) + G.nodes[node]['duration']

print("最早开始时间:")
print(earliest_start_time)

# 计算最晚开始时间
latest_start_time = {}
for node in nx.topological_sort(G):
    latest_start_time[node] = min([latest_start_time.get(succ, earliest_start_time[succ]) - G.nodes[node]['duration'] for succ in G.successors(node)], default=earliest_start_time[node])

print("最晚开始时间:")
print(latest_start_time)

# 计算关键路径
critical_paths = []
for path in nx.all_simple_paths(G, source='A', target='G'):
    is_critical = True
    for u, v in zip(path[:-1], path[1:]):
        if earliest_start_time[u] == latest_start_time[u] and earliest_start_time[v] == latest_start_time[v] and earliest_start_time[v] - latest_start_time[u] == G.edges[u, v]['duration']:
            continue
        else:
            is_critical = False
            break
    if is_critical:
        critical_paths.append(path)

print("关键路径:")
print(critical_paths)