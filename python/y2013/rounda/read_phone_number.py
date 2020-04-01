digit_to_value = {0 : "zero",
                  1 : "one",
                  2 : "two",
                  3 : "three",
                  4 : "four",
                  5 : "five",
                  6 : "six",
                  7 : "seven",
                  8 : "eight",
                  9 : "nine"}

repetition_value = {2 : "double",
                    3 : "triple",
                    4 : "quadruple",
                    5 : "quintuple",
                    6 : "sextuple",
                    7 : "septuple",
                    8 : "octuple",
                    9 : "nonuple",
                    10:  "decuple"}


def read_number(digit, format):
    i = 0
    output_string = ''
    for f in format:
        output_string += read_one_part(digit, i, i + f - 1)+' '
        i += f
    return output_string[0:-1]


def read_one_part(digit, start, end):
    cur_digit = digit[start]
    count = 1
    output_string = ''
    for i in range(start + 1, end + 2):
        if i > end or digit[i] != cur_digit:
            output_string += read_one_digit(cur_digit, count)+' '
            count = 1
            cur_digit = None if i > end else digit[i]
        else:
            count += 1
    return output_string[0:-1]


def read_one_digit(digit, repetition):
    if repetition in repetition_value:
        return repetition_value[repetition] + ' ' + digit_to_value[digit]
    output_string = ''
    for i in range(repetition):
        output_string += digit_to_value[digit] + ' '
    return output_string[0:-1]


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        digit_s, format_s = input().split(' ')
        digit = [int(s) for s in digit_s]
        format = [int(s) for s in format_s.split('-')]
        sol = read_number(digit, format)
        print('Case #{}: {}'.format(i, sol))
