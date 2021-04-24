def printPairs(arr, n, sum):

    # count = 0

    # Consider all possible
    # pairs and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")


# Driver Code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)


# sort & binary search
def pairedElements(arr, sum):

    low = 0
    high = len(arr) - 1

    while (low < high):
        if (arr[low] +
                arr[high] == sum):
            print("The pair is : (", arr[low],
                  ", ", arr[high], ")")
        if (arr[low] + arr[high] > sum):
            high -= 1
        else:
            low += 1


# Driver code
if __name__ == '__main__':

    arr = [2, 3, 4, -2,
           6, 8, 9, 11]
    arr.sort()
    pairedElements(arr, 6)


def find_pair(arr, k):
    seen = set()
    output = set()

    for i in arr:
        target = i-k
        if target not in seen:
            seen.add(i)
        else:
            output.add(i)

    print(len(output))


arr = [1, 3, 2, 2]
k = 4
find_pair(arr, k)
