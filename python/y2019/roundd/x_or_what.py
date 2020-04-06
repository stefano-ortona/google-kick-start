import heapq


def max_interval(a, q):
    a_star, even_ones = convert(a)
    left = [i for i in range(len(a)) if not a_star[i]]
    heapq.heapify(left)
    right = [-i for i in range(len(a)) if not a_star[i]]
    heapq.heapify(right)
    cur_len = len(a_star) if even_ones % 2 == 0 else max_len(len(a_star), left[0], -right[0])
    all_lengths = ''
    for index, new_el in q:
        new_el_eval = count_ones(new_el) % 2 == 0
        if new_el_eval != a_star[index]:
            even_ones = even_ones+1 if not new_el_eval else even_ones-1
            a_star[index] = new_el_eval
            if not new_el_eval:
                heapq.heappush(left, index)
                heapq.heappush(right, -index)
            clear_heap(left, a_star)
            clear_heap(right, a_star)
            cur_len = len(a_star) if even_ones % 2 == 0 else max_len(len(a_star), left[0], -right[0])
        all_lengths = all_lengths+str(cur_len)+' '
    return all_lengths[:-1]


def max_len(tot_len, left_el, right_el):
    return max([left_el, right_el, tot_len - right_el - 1, tot_len - left_el-1])


def clear_heap(heap, arr):
    mult = 1 if len(heap) == 0 or heap[0] >= 0 else -1
    while len(heap) > 0 and arr[mult * heap[0]]:
        heapq.heappop(heap)


def convert(a):
    out = [count_ones(num) % 2 == 0 for num in a]
    return out, sum([1 for i in out if not i])


def count_ones(num):
    return sum([1 for i in bin(num) if i == '1'])


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n, q_num = [int(s) for s in input().split(" ")]
        a = [int(s) for s in input().split(" ")]
        q = [[0, 0] for i in range(q_num)]
        for j in range(q_num):
            q[j] = [int(s) for s in input().split(" ")]
        sol = max_interval(a, q)
        print("Case #{}: {}".format(i, sol))
