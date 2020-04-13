def sort(numbers):
    odd = [x for x in numbers if x % 2 == 1]
    even = [x for x in numbers if x % 2 == 0]
    # sort
    odd.sort()
    even.sort(reverse=True)
    out_list = []
    odd_ind, even_ind = 0, 0
    for el in numbers:
        if el % 2 == 0:
            out_list.append(even[even_ind])
            even_ind += 1
        else:
            out_list.append(odd[odd_ind])
            odd_ind += 1
    return out_list


def from_list_to_string(list):
    out = ''
    for el in list:
        out = out + str(el) + " "
    return out[:-1]


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        input()
        elements = [int(s) for s in input().split(" ")]
        sol = sort(elements)
        print("Case #{}: {}".format(i, from_list_to_string(sol)))




