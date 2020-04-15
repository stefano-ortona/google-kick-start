def find_best_point(square):
    best_dis = -1
    best_x, best_y = 0, 0
    for s in square:
        cur_best_dist, cur_best_x, cur_best_y = -1, -1, -1
        for x in range(s[0], s[2] + 1):
            for y in range(s[1], s[3] + 1):
                cur_point_dis = 0
                for other in square:
                    cur_point_dis += tot_dis(x, y, other)
                if update_distance(cur_best_dist, cur_best_x, cur_best_y, cur_point_dis, x, y):
                    cur_best_dist, cur_best_x, cur_best_y = cur_point_dis, x, y
        if update_distance(best_dis, best_x, best_y, cur_best_dist, cur_best_x, cur_best_y):
            best_dis, best_x, best_y = cur_best_dist, cur_best_x, cur_best_y
    return [int(best_dis), best_x, best_y]


def update_distance(dis_or, x_or, y_or, new_dis, x_new, y_new):
    if dis_or == -1 or new_dis < dis_or:
        return True
    if dis_or < new_dis:
        return False
    # equal distances
    if x_new < x_or:
        return True
    if x_or < x_new:
        return False
    return y_new < y_or


def tot_dis(x, y, rec):
    x_c, y_c = closest_point(x, y, rec)
    vert = x_c == rec[0] or x_c == rec[2]
    horiz = y_c == rec[1] or y_c == rec[3]
    if not vert and not horiz:
        return tot_dis(x, y, [rec[0], rec[1], x, rec[3]]) + tot_dis(x, y, [x + 1, rec[1], rec[2], rec[3]])
    d = dis([x, y], [x_c, y_c])
    height = rec[3] - rec[1] + 1
    width = rec[2] - rec[0] + 1
    distance = (sub_n(d + width - 1) - sub_n(d - 1)) * height if vert \
        else (sub_n(d + height - 1) - sub_n(d - 1)) * width
    if vert:
        distance += sub_n(y_c - rec[1]) * width + sub_n(rec[3] - y_c) * width
    else:
        distance += sub_n(x_c - rec[0]) * height + sub_n(rec[2] - x_c) * height
    return distance


def sub_n(n):
    return n * (n + 1) / 2


def closest_point(x1, y1, rec):
    if rec[0] <= x1 <= rec[2] and rec[1] <= y1 <= rec[3]:
        return [x1, y1]
    if x1 <= rec[0]:
        return [rec[0], min(max(rec[1], y1), rec[3])]
    if y1 >= rec[3]:
        return [min(max(x1, rec[0]), rec[2]), rec[3]]
    if x1 >= rec[2]:
        return [rec[2], min(max(rec[1], y1), rec[3])]
    if y1 <= rec[1]:
        return [min(max(x1, rec[0]), rec[2]), rec[0]]


def dis(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def brute_force(square):
    best_dis, best_x, best_y = -1, -1, -1
    for one_s in square:
        for x in range(one_s[0], one_s[2] + 1):
            for y in range(one_s[1], one_s[3] + 1):
                cur_point_dis = 0
                for other_s in square:
                    for other_x in range(other_s[0], other_s[2] + 1):
                        for other_y in range(other_s[1], other_s[3] + 1):
                            cur_point_dis += dis([x, y], [other_x, other_y])
                if update_distance(best_dis, best_x, best_y, cur_point_dis, x, y):
                    best_dis, best_x, best_y = cur_point_dis, x, y
    return [int(best_dis), best_x, best_y]


if __name__ == '__main__':
    print(max([i for i in range(pow(10, 9))]))

    t = int(input())
    for i in range(1, t + 1):
        n_squares = int(input())
        squares = [[int(s) for s in input().split(" ")] for k in range(n_squares)]
        sol = find_best_point(squares)
        print("Case #{}: {} {} {}".format(i, sol[1], sol[2], sol[0]))
