def final_square(initial_row, initial_col, row, col, moves):
    n_dict = {}
    s_dict = {}
    e_dict = {}
    w_dict = {}
    make_move(n_dict, s_dict, w_dict, e_dict, initial_row, initial_col, row, col)
    for m in moves:
        cur_dict = n_dict
        d_row, d_col = initial_row - 1, initial_col
        if m == 'E':
            cur_dict = e_dict
            d_row, d_col = initial_row, initial_col + 1
        if m == 'W':
            cur_dict = w_dict
            d_row, d_col = initial_row, initial_col - 1
        if m == 'S':
            cur_dict = s_dict
            d_row, d_col = initial_row + 1, initial_col
        initial_row, initial_col = get_next_square(cur_dict, initial_row, initial_col, d_row, d_col)
        make_move(n_dict, s_dict, w_dict, e_dict, initial_row, initial_col, row, col)
    return [initial_row, initial_col]


def get_next_square(curr_dict, row, col, d_row, d_col):
    return curr_dict.get((row, col), (d_row, d_col))


def make_move(n_dict, s_dict, w_dict, e_dict, row, col, row_len, col_len):
    if row > 0:
        default_to = None if row == row_len - 1 else (row + 1, col)
        update_dict(n_dict.get((row, col), -1), s_dict.get((row, col), -1), s_dict, (row-1, col), default_to)
    if row < row_len - 1:
        default_to = None if row == 0 else (row - 1, col)
        update_dict(s_dict.get((row, col), -1), n_dict.get((row, col), -1), n_dict, (row+1, col), default_to)
    if col > 0:
        default_to = None if col == col_len - 1 else (row, col + 1)
        update_dict(w_dict.get((row, col), -1), e_dict.get((row, col), -1), e_dict, (row, col-1), default_to)
    if col < col_len - 1:
        default_to = None if col == 0 else (row, col - 1)
        update_dict(e_dict.get((row, col), -1), w_dict.get((row, col), -1), w_dict, (row, col+1), default_to)


def update_dict(from_val, to_val, curr_dict, default_from, default_to):
    if from_val is None:
        return
    from_val = default_from if from_val == -1 else from_val
    to_val = default_to if to_val == -1 else to_val
    curr_dict[from_val] = to_val


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n, r, c, init_row, init_col = [int(s) for s in input().split(" ")]
        moves = input()
        sol = final_square(init_row - 1, init_col - 1, r, c, moves)
        print("Case #{}: {} {}".format(i, sol[0] + 1, sol[1] + 1))