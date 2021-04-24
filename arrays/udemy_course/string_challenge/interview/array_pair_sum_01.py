def find_sum_pairs(num, target):
    extra = {}
    result = []
    for i in range(len(num)):
        tmp = target-num[i]
        if tmp in extra:
            result.append((num[extra[tmp]], num[i]))
        extra[num[i]] = i
    print(result)


num = [1, 3, 2, 2, 5, 7]
(find_sum_pairs(num, 4))
