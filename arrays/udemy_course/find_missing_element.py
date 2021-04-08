def find_missing_element(arr1, arr2):
    count = {}
    for element in arr1:
        if element in count:
            count[element] += 1
        else:
