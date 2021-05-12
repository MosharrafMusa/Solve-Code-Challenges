def array_pair_sum(arr1, s):
    seen= {}
    result = []

    for i in range(len(arr1)):
        target = s - arr1[i]
        if target in seen:
            result.append((arr1(seen[temp]), arr1[i]))
        else:
            seen(arr1[i]) = i

    return result

arr1 = [1,3,2,2,5]
print(array_pair_sum(arr1, 4))