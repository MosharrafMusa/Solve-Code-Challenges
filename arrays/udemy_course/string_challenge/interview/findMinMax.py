def Range(list1):
    largest = list1[0]
    lowest = list1[0]

    for item in list1[1:]:
        if item > largest:
            largest = item

        if item < lowest:

            lowest = item

    print("Largest element is:", largest)
    print("Smallest element is:", lowest)


# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list1)
