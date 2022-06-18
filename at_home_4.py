def triple(lst):
    for i in range(len(lst)):
        lst[i] *= 3
    return lst


def map(func, data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = func(data[i])
    return res


def pow(num1, num2):
    return num1 ** num2


def map2(func, data1, data2):
    if len(data1) == len(data2):
        res = [None] * len(data1)
        for i in range(len(data1)):
            res[i] = func(data1[i], data2[i])
        return res
    else:
        raise IndexError("lengths of data1 and data2 have to be the same!")


print(list(map(triple, ([1, 10, 100], [2, 20, 200], [3, 30, 300]))))
print(list(map2(pow, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
