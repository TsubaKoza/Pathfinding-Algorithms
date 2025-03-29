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
unsearched_nodes = list(range(node_num))
searched_nodes = []
distance = [math.inf] * node_num
previous_nodes = [-1] * node_num
distance[0] = 0

def get_target_min_index(min_index, distance, unsearched_nodes):
    start = 0
    while True:
        index = distance.index(min_index, start)
        if index in unsearched_nodes:
            return index
        else:
            start = index + 1

while len(unsearched_nodes) != 0:
    posible_min_distance = math.inf
    for node_index in unsearched_nodes:
        if posible_min_distance > distance[node_index]:
            posible_min_distance = distance[node_index]
    target_min_index = get_target_min_index(posible_min_distance, distance, unsearched_nodes)
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
