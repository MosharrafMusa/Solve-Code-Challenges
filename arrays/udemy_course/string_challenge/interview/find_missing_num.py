def find_missing(lst):
    # return [x for x in range(lst[0], lst[-1]+1)
    #                            if x not in lst]

    for i in range(lst[0], lst[-1]+1):
        if i not in lst:
            print(i)


# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
find_missing(lst)
