# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    if x1 < x2 and v1 < v2:
        return('NO')
    if x1 > x2 and v1 > v2:
        return('NO')

    x1_list = list()
    for x in range(10000):
        x1_list.append({x:x1})
        x1 += v1

    x2_list = list()
    for x in range(10000):
        x2_list.append({x:x2})
        x2 += v2

    # compare
    for x in range(10000):
        xone = x1_list[x]
        xtwo = x2_list[x]
        if xone == xtwo:
            return('YES')

    return('NO')

# 112 9563 8625 244
x1 = 112
v1 = 9563
x2 = 8625
v2 = 2442

print(kangaroo(x1, v1, x2, v2))
