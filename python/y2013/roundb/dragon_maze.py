def shortest_path(start, end, maze):
    visited = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
    visited[start[0]][start[1]] = True
    to_visit = [[start[0], start[1], maze[start[0]][start[1]]]]
    while len(to_visit) > 0:
        next_nodes_size = len(to_visit)
        next_neighs = []
        for k in range(next_nodes_size):
            i, j, cost = to_visit.pop()
            if i == end[0] and j == end[1]:
                return cost
            append_neigh(i + 1, j, cost, next_neighs, maze)
            append_neigh(i - 1, j, cost, next_neighs, maze)
            append_neigh(i, j + 1, cost, next_neighs, maze)
            append_neigh(i, j - 1, cost, next_neighs, maze)
        filter_neighbours(next_neighs, to_visit, visited)
    return -1


def append_neigh(i, j, cost, next_neighs, maze):
    if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] != -1:
        next_neighs.append((cost + maze[i][j], i, j))


def filter_neighbours(next_neighs, to_visit, visited):
    next_neighs.sort(reverse=True)
    for cost, i, j in next_neighs:
        if not visited[i][j]:
            to_visit.append([i, j, cost])
            visited[i][j] = True


if __name__ == '__main__':

    t = int(input())
    for iteration in range(1, t + 1):
        row, col = [int(s) for s in input().split(" ")]
        x_s, y_s, x_e, y_e = [int(s) for s in input().split(" ")]
        input_maze = [[int(s) for s in input().split(" ")] for k in range(row)]
        sol = shortest_path([x_s, y_s], [x_e, y_e], input_maze)
        sol_string = "Mission Impossible." if sol == -1 else str(sol)
        print("Case #{}: {}".format(iteration, sol_string))
