

def remove_dup(l1):
    res = []
    for i in l1:
        if i not in res:
            res.append(i)

    print(res)


l1 = [1, 3, 5, 6, 3, 5, 6, 1]
l2 = [1, 3, 5, 6, 3, 5, 6, 1]
remove_dup(l1)


def remove_dup1(l2):
    return list(set(l2))


print(remove_dup1(l2))
