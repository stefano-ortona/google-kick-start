def max_board(board, k):
    max_min_diff = compute_max_min_diff(board)
    max_area = len(board)
    for i in range(len(board)):
        for start in range(len(board[0]) - 1):
            for end in range(start + 1, len(board[0])):
                max_area = max(max_area, expand_row(i, k, start, end, max_min_diff))
    return max_area


def expand_row(row, k, start, end, max_min_diff):
    cur_area = 0
    while row < len(max_min_diff) and max_min_diff[row][start][end] <= k:
        cur_area += end - start + 1
        row += 1
    return cur_area


def compute_max_min_diff(board):
    max_min_diff = {}
    for row in range(len(board)):
        cur_board = [[0 for j in range(len(board[0]))] for i in range(len(board[0]))]
        for i in range(len(board[0]) - 1):
            min_el = board[row][i]
            max_el = board[row][i]
            for j in range(i + 1, len(board[0])):
                min_el = min(min_el, board[row][j])
                max_el = max(max_el, board[row][j])
                cur_board[i][j] = max_el - min_el
        max_min_diff[row] = cur_board
    return max_min_diff


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        r, c, k = [int(s) for s in input().split(' ')]
        board = [[0 for j in range(c)] for i in range(r)]
        for j in range(r):
            board[j] = [int(s) for s in input().split(' ')]
        sol = max_board(board, k)
        print("Case #{}: {}".format(i, sol))
