def pick_plates(stack, p):
    stack = cumulative_sum(stack)
    mem = [[0 for x in range(p+1)] for y in range(len(stack))]
    return pick_plates_recursive(stack, 0, mem, p)


def pick_plates_recursive(stack, index, mem, remaining):
    if index >= len(stack) or remaining == 0:
        return 0
    if mem[index][remaining] != 0:
        return mem[index][remaining]
    min_index = min(remaining, len(stack[index])) - 1
    max_value = 0
    # try to pick from current stack
    for i in range(min_index, -1, -1):
        max_value = max(max_value, stack[index][i] + pick_plates_recursive(stack, index+1, mem, remaining - (i + 1)))
    # do not pick from current stack
    max_value = max(max_value, pick_plates_recursive(stack, index+1, mem, remaining))
    mem[index][remaining] = max_value
    return max_value


def cumulative_sum(stack):
    for i in range(len(stack)):
        for j in range(1, len(stack[i])):
            stack[i][j] = stack[i][j-1] + stack[i][j]
    return stack


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n, k, p = [int(s) for s in input().split(" ")]
        stack = [[0 for x in range(k)] for y in range(n)]
        for j in range(n):
            stack[j] = [int(s) for s in input().split(" ")]
        sol = pick_plates(stack, p)
        print("Case #{}: {}".format(i, sol))