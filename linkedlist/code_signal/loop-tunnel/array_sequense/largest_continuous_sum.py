def largest_cont_sum(arr):

    #     edge case
    if len(arr) == 0:
        return 0

    cur_sum = max_sum = arr[0]

    for num in arr[1:]:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(cur_sum, max_sum)

    return max_sum


print(largest_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
