def number_palindromes(string, question):
    occ_dict = build_occ_dictionary(string)
    count = 0
    for i in range(len(question)):
        l, r = question[i]
        if 0 < l <= len(string) and len(string) >= r >= l and is_palindrome(occ_dict[l - 1], occ_dict[r]):
            count += 1
    return count


def is_palindrome(occ_dict_first, occ_dict_second):
    dict_copy = dict(occ_dict_second)
    for i in occ_dict_first:
        dict_copy[i] -= occ_dict_first[i]
    return sum([1 for x in dict_copy if dict_copy[x] % 2 == 1]) <= 1


def build_occ_dictionary(string):
    occ_dict = {}
    count = 1
    index_dict = {0: {}}
    for char in string:
        val = occ_dict.get(char, 0) + 1
        occ_dict[char] = val
        dict_copy = dict(occ_dict)
        index_dict[count] = dict_copy
        count += 1
    return index_dict


if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        n, q = [int(s) for s in input().split(" ")]
        string = input()
        question = [[0, 0] for x in range(q)]
        for j in range(q):
            question[j] = [int(s) for s in input().split(" ")]
        sol = number_palindromes(string, question)
        print("Case #{}: {}".format(i, sol))
