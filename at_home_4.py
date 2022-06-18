def func(num):
    return num * 3


def map(function, data):
    new_data = [None] * len(data)
    for i in range(len(data)):
        new_data[i] = function(data[i])
    return new_data


def triple(data):
    return map(func, data)


def is_number(a, b, c):
    if isinstance((a, b, c), int):
        return True
    return False


def sum(a, b, c):
    return a + b + c


def mult(a, b, c):
    return a * b * c


def map3(func, data1, data2, data3):
    if len(data1) == len(data2) == len(data3):
        res = [None] * len(data1)
        for i in range(len(data1)):
            res[i] = func(data1[i], data2[i], data3[i])
        return res
    else:
        raise IndexError("Lengths of data1, data2 and data3 have to be the same!")


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
print(map3(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
print(map3(mult, [1, 2, 3], [10, 20, 30], [100, 200, 300]))

