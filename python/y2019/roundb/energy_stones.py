from functools import cmp_to_key


def max_energy(stones):
    stones = sorted(stones, key=cmp_to_key(sorting_stones))
    max_time = sum(x[0] for x in stones)
    mem = [[-1 for j in range(max_time + 1)] for i in range(len(stones))]
    return max_energy_so_far(stones, 0, 0, mem)


def max_energy_so_far(stones, index, time, mem):
    if index >= len(stones):
        return 0
    if mem[index][time] != -1:
        return mem[index][time]
    # do not pick current stone
    max_value = max_energy_so_far(stones, index + 1, time, mem)
    # pick current stones only if admissible
    energy_left = stones[index][1] - time * stones[index][2]
    if energy_left > 0:
        max_value = max(max_value, energy_left + max_energy_so_far(stones, index + 1, time + stones[index][0], mem))
    mem[index][time] = max_value
    return max_value


def sorting_stones(x, y):
    return x[0]*y[2] - y[0]*x[2]


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        stones = [[0, 0, 0] for j in range(n)]
        for j in range(n):
            stones[j] = [int(x) for x in input().split(' ')]
        sol = max_energy(stones)
        print('Case #{}: {}'.format(i, sol))

