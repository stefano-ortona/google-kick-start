from bisect import bisect_left


def min_difficulty(times, k):
    if len(times) == 0:
        return 0
    key_value = {}
    for i in range(0, len(times) - 1):
        key = times[i + 1] - times[i]
        key_value[key] = key_value.get(key, 0) + 1
    return iterate_dictionary(key_value, k)


def iterate_dictionary(key_value, k):
    sorted_keys = sorted(key_value)
    curr_key = len(sorted_keys) - 1
    while sorted_keys[curr_key] > 1:
        el = sorted_keys[curr_key]
        if key_value[el] > k:
            return el
        k -= key_value[el]
        new_el = [el // 2, el - (el // 2)]
        curr_key -= 1
        for one_el in new_el:
            if one_el not in key_value:
                key_value[one_el] = 0
                sorted_keys.insert(bisect_left(sorted_keys, one_el), one_el)
                curr_key += 1
            key_value[one_el] += key_value[el]
    return 1


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        times = [int(s) for s in input().split(" ")]
        sol = min_difficulty(times, k)
        print("Case #{}: {}".format(i, sol))
