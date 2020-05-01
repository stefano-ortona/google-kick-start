number_digs = {0: '1111110', 1: '0110000', 2: '1101101', 3: '1111001', 4: '0110011', 5: '1011011', 6: '1011111',
               7: "1110000", 8: "1111111", 9: "1111011"}


def next_digit(digits):
    sol = []
    for i in range(10):
        cur_num, mask = i, [1, 1, 1, 1, 1, 1, 1]
        for one_digit in digits:
            mask = apply_and_compare(mask, one_digit, cur_num) if mask is not None else None
            cur_num = cur_num - 1 if cur_num > 0 else 9
        if mask is not None:
            sol.append(apply_mask(mask, cur_num))
    return None if len(sol) != 1 else sol[0]


def apply_and_compare(mask, digit, target_num):
    actual_digit = apply_mask(mask, target_num)
    for i in range(len(digit)):
        if digit[i] == '1' and actual_digit[i] == '0':
            return None
        if digit[i] == '0' and actual_digit[i] == '1':
            mask[i] = 0
    return mask


def apply_mask(mask, num):
    mask_as_string = "".join(map(str, mask))
    return format(int(mask_as_string, 2) & int(number_digs[num], 2), '07b')


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        t_digits = [s for s in input().split(" ")][1:]
        t_sol = next_digit(t_digits)
        t_sol = t_sol if t_sol is not None else "ERROR!"
        print("Case #{}: {}".format(i, t_sol))
