from heapq import *


def shortest_path(from_node, to_node, colours, dir_matrix, tot_nodes):
    # Find shortest path between two nodes with Dijkstra's algorithm
    color_map = build_color_proximity(colours)
    neigh = build_neigh(dir_matrix)
    min_dist = [-1 for i in range(tot_nodes + 1)]
    min_dist[from_node] = 0
    heap = []
    add_to_heap(from_node, neigh, color_map, colours[from_node], heap, min_dist)
    while len(heap) > 0:
        while len(heap) > 0 and min_dist[heap[0][1]] != -1:
            heappop(heap)
        if len(heap) > 0:
            cost, next_n = heappop(heap)
            min_dist[next_n] = cost
            if next_n == to_node:
                break
            add_to_heap(next_n, neigh, color_map, colours[next_n], heap, min_dist)
    return min_dist[to_node]


def add_to_heap(node, neigh, color_map, cur_color, heap, min_dist):
    all_neigh = neigh.get(node, [])
    for one_n in all_neigh:
        if min_dist[one_n[0]] == -1:
            heappush(heap, (min_dist[node] + one_n[1], one_n[0]))
    all_color_neigh = color_map.get(cur_color, [])
    for one_n in all_color_neigh:
        if min_dist[one_n] == -1:
            heappush(heap, (min_dist[node], one_n))


def build_color_proximity(colors):
    color_dict = {}
    for i in range(len(colors)):
        cur_col = colors[i]
        room_list = color_dict.get(cur_col, [])
        room_list.append(i)
        color_dict[cur_col] = room_list
    return color_dict


def build_neigh(dir_matrix):
    neigh = {}
    for el in dir_matrix:
        from_node, to_node, cost = el
        cur_neigh = neigh.get(from_node, [])
        cur_neigh.append([to_node, cost])
        neigh[from_node] = cur_neigh
    return neigh


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        room_num = int(input())
        colours = [input() for j in range(room_num)]
        colours.insert(0, 'None')
        edges_num = int(input())
        dir_matrix = []
        for j in range(edges_num):
            dir_matrix.append([int(s) for s in input().split(" ")])
        num_paths = int(input())
        print("Case #{}:".format(i))
        for j in range(num_paths):
            to_node, from_node = [int(s) for s in input().split(" ")]
            sol = shortest_path(to_node, from_node, colours, dir_matrix, room_num)
            print(sol)
