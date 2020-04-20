directions = {"W": (0, -1), "E": (0, 1), "N": (1, -1), "S": (1, 1)}
index = 0
base = 1000000000


def final_square(program_string):
    global index
    index = 0
    final_pos = compute_moves(1, program_string)
    return [determine_final_pos(final_pos[0] + 1), determine_final_pos(final_pos[1] + 1)]


def determine_final_pos(position):
    if position > base:
        return position % base
    elif position <= 0:
        return base - (abs(position) % base)
    return position


def compute_moves(repetition, program_string):
    moves = [0, 0]
    global index
    while index < len(program_string) and program_string[index] != ')':
        cur_char = program_string[index]
        index += 1
        if cur_char in directions:
            cur_dir = directions[cur_char]
            moves[cur_dir[0]] += cur_dir[1]
        else:
            # recursion, cur char must be a number
            index += 1
            recur_moves = compute_moves(int(cur_char), program_string)
            moves[0] += recur_moves[0]
            moves[1] += recur_moves[1]
    # end of current program
    index += 1
    return [moves[0] * repetition, moves[1] * repetition]


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        program = input()
        sol = final_square(program)
        print("Case #{}: {} {}".format(i, sol[0], sol[1]))
