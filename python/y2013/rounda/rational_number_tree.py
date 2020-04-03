def find_level_position_by_index(index):
    level = 1
    cur_numb = 1
    next_numb = 2
    while not(cur_numb <= index < next_numb):
        cur_numb = next_numb
        next_numb *= 2
        level += 1
    return [level, index - cur_numb]


class NumberTree:

    def find_number_by_index(self, index):
        level, pos = find_level_position_by_index(index)
        return self.find_number(level, pos)

    def find_index_by_number(self, p, q):
        level, pos = self.find_level_position(p, q)
        return pow(2, level) + pos

    def find_level_position(self, p, q):
        if p == 1 and q == 1:
            return [0, 0]
        father_p, father_q = p, q - p
        increment = 0
        if p > q:
            father_p, father_q = p - q, q
            increment = 1
        level, pos = self.find_level_position(father_p, father_q)
        return [level + 1, pos * 2 + increment]

    def find_number(self, level, position):
        if position == 0:
            return [1, level]
        p, q = self.find_number(level - 1, position // 2)
        if position % 2 == 0:
            # left child
            return [p, p+q]
        return [p+q, q]


if __name__ == '__main__':

    t = int(input())
    tree = NumberTree()
    for i in range(1, t + 1):
        in_numbers = [int(s) for s in input().split(' ')]
        if in_numbers[0] == 1:
            sol = tree.find_number_by_index(in_numbers[1])
            print('Case #{}: {} {}'.format(i, sol[0], sol[1]))
        else:
            sol = tree.find_index_by_number(in_numbers[1], in_numbers[2])
            print('Case #{}: {}'.format(i, sol))
