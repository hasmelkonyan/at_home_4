def mult_by_three(num):
    return num * 3


def map3(func, data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = func(data[i])
    return res


def triple(data):
    return map3(mult_by_three, data)


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


print(triple([1, 10, 300]))
print(list(map2(pow, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
