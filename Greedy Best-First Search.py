import math

route_list = [
    [0, 3, 1, 4, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 7],
    [0, 0, 0, 0, 2, 3, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

node_num = len(route_list)

def get_heuristic(x_i, y_i):
    return 60 * math.sqrt((x_i - 35.6864604) ** 2 + (y_i - 139.7635769) ** 2)

unsearched_nodes = list(range(node_num))
searched_nodes = []
heuristic = [
    get_heuristic(35.6989227, 139.70764),
    get_heuristic(35.728926, 139.71038),
    get_heuristic(35.691574, 139.704647),
    get_heuristic(35.7012623, 139.7467247),
    get_heuristic(35.6915961, 139.7378098),
    get_heuristic(35.6844237, 139.7300108),
    get_heuristic(35.6954496, 139.7514154),
    get_heuristic(35.6864604, 139.7635769)
]

previous_nodes = [-1] * node_num
distance = [math.inf] * node_num
distance[0] = 0

def get_best_node(unsearched_nodes, heuristic):
    best_node = unsearched_nodes[0]
    best_value = heuristic[best_node]
    for node in unsearched_nodes:
        if heuristic[node] < best_value:
            best_node = node
            best_value = heuristic[node]
    return best_node

while len(unsearched_nodes) != 0:
    target_min_index = get_best_node(unsearched_nodes, heuristic)
    searched_nodes.append(target_min_index)
    unsearched_nodes.remove(target_min_index)

    target_edge = route_list[target_min_index]
    for index, route_dis in enumerate(target_edge):
        if route_dis != 0:
            if distance[index] > distance[target_min_index] + route_dis:
                distance[index] = distance[target_min_index] + route_dis
                previous_nodes[index] = target_min_index

print("-----経路-----")
previous_node = node_num - 1
while previous_node != -1:
    if previous_node != 0:
        print(f"{previous_node} <- ", end='')
    else:
        print(previous_node)
    previous_node = previous_nodes[previous_node]

print("-----探索されたノード-----")
print(searched_nodes)

print("-----距離-----")
print(distance[node_num - 1])
