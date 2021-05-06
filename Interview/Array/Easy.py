# Array Pair sum
def array_pair_sum(arr1, s):
    seen = {}
    result = []
    for i in range(len(arr1)):
        temp = s-arr1[i]
        if temp in seen:
            result.append((arr1[seen[temp]], arr1[i]))

        else:
            seen[arr1[i]] = i
    return result


arr1 = [1, 2, 3, 2, 5, 0, 4]
s = 4
print(array_pair_sum(arr1, s))
