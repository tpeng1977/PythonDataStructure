import copy


def filter_list(in_list):
    res = copy.deepcopy(in_list)
    for i in in_list:
        if type(i) != int:
            res.remove(i)
    return res


print(filter_list([1, 2, 3, "a", "b", "c", "d", "e", 4]))


def f(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * f(n - 1)


for i in range(2**3):
    print(f(i), end=" ")

